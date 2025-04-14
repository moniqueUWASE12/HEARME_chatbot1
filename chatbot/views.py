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



# Initialize the ChatBot
bot = ChatBot(
    'HearMe',
    read_only=False,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "I'm here to listen. Could you tell me more about what you're experiencing?",
            'maximum_similarity_threshold': 0.75,  # Slightly lowered to catch more variations
            'statement_comparison_function': LevenshteinDistance,
            'response_selection_method': get_most_frequent_response
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'help me',
            'output_text': "I'm here to help. What's troubling you today?"
        }
    ],

    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.convert_to_ascii',
        'chatterbot.preprocessors.unescape_html'
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
    user_conversations = Conversation.objects.filter(user=request.user).order_by('timestamp')
    
    # Group conversations into sessions (optional enhancement)
    chat_data = [
        {'message': conv.message, 'response': conv.response, 'timestamp': conv.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        for conv in user_conversations
    ]
    return render(request, 'chatbot/index.html', {
        'username': request.user.username,
        'chat_data': chat_data
    })

    


def chatbot_ai_response(request):
    user_input = request.POST.get('user_input', '')
    user_input_lower = user_input.lower()

    # Analyze sentiment
    sentiment = TextBlob(user_input).sentiment
    polarity = sentiment.polarity
    sentiment_label = "Neutral"
    if polarity > 0.1:
        sentiment_label = "Positive"
    elif polarity < -0.1:
        sentiment_label = "Negative"

    # Check for therapist recommendation keywords
    if "therapist" in user_input_lower or "recommend" in user_input_lower:
        therapists = Therapist.objects.all()[:3]  # Fetch up to 3 entries
        if therapists:
            recs = []
            for therapist in therapists:
                rec = f"{therapist.name} ({therapist.specialization}) - {therapist.location}. Call: {therapist.phone}"
                recs.append(rec)
            response_text = "Here are some therapist recommendations: " + " | ".join(recs)
        else:
            response_text = "I'm sorry, I don't have any therapist recommendations at the moment."

    # Check for video request keywords
    elif "video" in user_input_lower or "watch" in user_input_lower:
        videos = Video.objects.all()[:1]  # Fetch one video recommendation
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
        # Standard chatbot response
        bot_response = bot.get_response(user_input)
        response_text = str(bot_response)

    #response_text += f"\n\n🧠 Sentiment Analysis: {sentiment_label} (Polarity: {polarity:.2f})"
    
    # Save the conversation
    if request.user.is_authenticated:
        Conversation.objects.create(user=request.user, message=user_input, response=response_text)
        return JsonResponse({'ai_response': response_text})
    
    

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