from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login  # Import authenticate and login
from django.contrib import messages  # Import messages for error handling
from chatterbot import ChatBot
from .models import Therapist, Video
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import UserProfile, Conversation
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_most_frequent_response
from textblob import TextBlob
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from django.utils import timezone
from datetime import timedelta
import time
# Import your new model
from .models import ConversationSession
from django.core.cache import cache
from nltk.sentiment import SentimentIntensityAnalyzer
from django.views.decorators.cache import cache_page


# Initialize chatbot (no training here!)
bot = ChatBot(
    'HearMe',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3',  # Shared DB with Django
    read_only=True,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "I'm here to listen. Could you tell me more about what you're experiencing?",
            'maximum_similarity_threshold': 0.95,
            'statement_comparison_function': LevenshteinDistance,
            'response_selection_method': get_most_frequent_response
        }
    ]
)



def welcome_view(request):
    return render(request, 'chatbot/welcome.html')

def landing_view(request):
    return render (request, 'chatbot/landing.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)  # Authenticate user
        if user is not None:
            login(request, user)  # Log the user in
            return redirect("chatbot_view")  # Redirect to the landing.html view
        else:
            messages.error(request, "Invalid username or password.")  # Display error message
    return render(request, 'chatbot/login.html')


def signup_view(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        location = request.POST.get("location")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("signup")
        
        user = User.objects.create_user(username=username, email=email, password=password1, first_name=fullname)
        user.is_active = True
        user.save()

         # Create the user profile
        UserProfile.objects.create(user=user, phone=phone, location=location)

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect("login")


    return render(request, "chatbot/signup.html")


@login_required
def chatbot_view(request):
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)
    seven_days_ago = today - timedelta(days=7)

    conversations_today = Conversation.objects.filter(user=request.user, timestamp__date=today)
    conversations_yesterday = Conversation.objects.filter(user=request.user, timestamp__date=yesterday)
    conversations_last_week = Conversation.objects.filter(
        user=request.user,
        timestamp__date__gte=seven_days_ago,
        timestamp__date__lt=yesterday
    )

    chat_data = [
        {'message': conv.message, 'response': conv.response, 'timestamp': conv.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        for conv in conversations_today  # You can switch to show all if needed
    ]

    return render(request, 'chatbot/index.html', {
        'username': request.user.username,
        'chat_data': chat_data,
        'conversations_today_count': conversations_today.count(),
        'conversations_yesterday_count': conversations_yesterday.count(),
        'conversations_last_week_count': conversations_last_week.count(),
    })
def create_session_title(user_input):
    """
    Generates a title from the user's first message.
    You can use more advanced methods (like NLP summarization) here.
    For now, we simply return the first 40 characters.
    """
    title = user_input.strip()
    if len(title) > 40:
        title = title[:40] + "..."
    return title or "New Conversation"  
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(user_input):
    scores = analyzer.polarity_scores(user_input)
    if scores['compound'] > 0.1:
        return "Positive"
    elif scores['compound'] < -0.1:
        return "Negative"
    return "Neutral"  

@cache_page(60 * 1)
def chatbot_ai_response(request):
    start_time = time.time()
    user_input = request.POST.get('user_input', '').strip()
    user_input_lower = user_input.lower()
    cache_key = f"chatbot_response_{user_input}"
    cached_response = cache.get(cache_key)

    if cached_response:
        return JsonResponse({'ai_response': cached_response})
    
    # Sentiment Analysis
    sentiment_label = analyze_sentiment(user_input)



    # Therapist Recommendation
    if "therapist" in user_input_lower or "recommend" in user_input_lower:
        therapists = get_cached_therapists()
        if therapists:
            recs = [
                f"{t.name} ({t.specialization}) - {t.location}. Call: {t.phone}"
                for t in therapists
            ]
            response_text = "Here are some therapist recommendations: " + " | ".join(recs)
        else:
            response_text = "I'm sorry, I don't have any therapist recommendations at the moment."

    # Video Recommendation
    elif "video" in user_input_lower or "watch" in user_input_lower:
        videos = get_cached_videos()
        if videos:
            video = videos[0]
            response_text = (
                f"Here's a video you might find helpful:\n\n"
                f"Title: {video.title}\n"
                f"Description: {video.description}\n"
                f"Watch here: {video.video_url}"
            )
        else:
            response_text = "I'm sorry, I don't have any video recommendations at the moment."
    else:
        bot_start = time.time()
        bot_response = bot.get_response(user_input)
        response_text = str(bot_response)

    # Save conversation
    if request.user.is_authenticated:
        today = timezone.now().date()
        session = ConversationSession.objects.filter(user=request.user, start_time__date=today).last()
        if not session:
            session_title = create_session_title(user_input)
            session = ConversationSession.objects.create(user=request.user, title=session_title)
        Conversation.objects.create(user=request.user, session=session, message=user_input, response=response_text)
        cache.set(cache_key, response_text, timeout=3600)

        total_duration = time.time() - start_time
        print(f"[DEBUG] Total chatbot_ai_response time: {total_duration:.4f} seconds")

        return JsonResponse({'ai_response': response_text})
    else:
        return JsonResponse({'ai_response': "Sorry, something went wrong. Please log in and try again."}, status=403)
def get_cached_therapists():
    therapists = cache.get('therapist_recommendations')
    if not therapists:
        therapists = list(Therapist.objects.only('name', 'specialization', 'location', 'phone')[:3])
        cache.set('therapist_recommendations', therapists, timeout=3600)  # Cache for 1 hour
    return therapists

def get_cached_videos():
    videos = cache.get('video_recommendations')
    if not videos:
        videos = list(Video.objects.only('title', 'description', 'video_url')[:1])
        cache.set('video_recommendations', videos, timeout=3600)  # Cache for 1 hour
    return videos

def custom_logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page

def get_response(message):
    response = bot.get_response(message)
    return str(response)

# Example usage
if __name__ == "__main__":
    print("HearMe is ready! Type 'exit' to end the conversation.")
    print("Bot: Hi, I'm HearMe. How are you feeling today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Take care of yourself. I'm always here when you need to talk.")
            break
        
        response = get_response(user_input)
        print(f"Bot: {response}")


@login_required
def load_session_view(request):
    session_id = request.GET.get("session_id")
    try:
        session = ConversationSession.objects.get(id=session_id, user=request.user)
        # Get all conversation messages for this session
        convs = Conversation.objects.filter(session=session).order_by('timestamp')
        messages_data = []
        for conv in convs:
            # You can decide what to include here – for now, include type and text
            messages_data.append({
                "type": "user",
                "text": conv.message,
            })
            messages_data.append({
                "type": "ai",
                "text": conv.response,
            })
        return JsonResponse({"messages": messages_data})
    except ConversationSession.DoesNotExist:
        return JsonResponse({"error": "Session not found."}, status=404)
    
def get_recent_conversations(request):
    if request.user.is_authenticated:
        # Fetch recent conversation sessions for the logged-in user
        sessions = ConversationSession.objects.filter(user=request.user).order_by('-start_time')[:10]
        recent_conversations = [
            {
                'id': session.id,
                'title': session.title,
                'start_time': session.start_time.strftime('%Y-%m-%d %H:%M:%S')
            }
            for session in sessions
        ]
        return JsonResponse({'recent_conversations': recent_conversations})
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=403)

  