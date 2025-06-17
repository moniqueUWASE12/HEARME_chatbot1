from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Therapist, Video, UserProfile, Conversation, ConversationSession, Hospital
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from textblob import TextBlob
from django.utils import timezone
from datetime import timedelta
import time
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from nltk.sentiment import SentimentIntensityAnalyzer
from django.views.decorators.cache import cache_page
from django.utils.text import Truncator
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import logging
import json
import re
import random
import nltk
nltk.download('vader_lexicon')  # <--- Add this line


# Initialize logger
logger = logging.getLogger(__name__)

# Load the trained GPT-2 model and tokenizer
model_path = "chatbot/models/gpt2-hearme"
gpt2_model = AutoModelForCausalLM.from_pretrained(model_path)
gpt2_tokenizer = AutoTokenizer.from_pretrained(model_path)

# Initialize the text-generation pipeline
gpt2_pipeline = pipeline("text-generation", model=gpt2_model, tokenizer=gpt2_tokenizer)

# Load intents from intents.json
with open("chatbot/intents/intents.json", "r") as file:
    intents = json.load(file)["intents"]

def match_intent(user_input):
    for intent in intents:
        for pattern in intent["patterns"]:
            if re.search(rf"\b{re.escape(pattern.lower())}\b", user_input.lower()):
                return random.choice(intent["responses"])
    return None

def generate_gpt2_response(user_input):
    try:
        response = gpt2_pipeline(user_input, max_length=50, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        logger.error(f"Error generating GPT-2 response: {e}")
        return "I'm sorry, I couldn't process your request."

def generate_response(user_input):
    intent_response = match_intent(user_input)
    if intent_response:
        return intent_response
    return generate_gpt2_response(user_input)

def welcome_view(request):
    return render(request, 'chatbot/welcome.html')

def landing_view(request):
    return render(request, 'chatbot/landing.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("chatbot_view")
        else:
            messages.error(request, "Invalid username or password.")
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

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("signup")
        
        user = User.objects.create_user(username=username, email=email, password=password1, first_name=fullname)
        user.is_active = True
        user.save()

        UserProfile.objects.create(user=user, phone=phone, location=location)

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect("login")

    return render(request, "chatbot/signup.html")

@login_required
def chatbot_view(request):
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)
    seven_days_ago = today - timedelta(days=7)

    sessions_today = ConversationSession.objects.filter(user=request.user, start_time__date=today)
    sessions_yesterday = ConversationSession.objects.filter(user=request.user, start_time__date=yesterday)
    sessions_last_week = ConversationSession.objects.filter(
        user=request.user,
        start_time__date__gte=seven_days_ago,
        start_time__date__lt=yesterday
    )
    session_groups = [
        {'label': 'Today', 'sessions': sessions_today},
        {'label': 'Yesterday', 'sessions': sessions_yesterday},
        {'label': 'Last 7 Days', 'sessions': sessions_last_week},
    ]

    return render(request, 'chatbot/index.html', {
        'username': request.user.username,
        'session_groups': session_groups,
    })

def create_session_title(user_input):
    title = user_input.strip()
    return Truncator(title).chars(40) or "New Conversation"

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"
@csrf_exempt
@login_required
@cache_page(60 * 1)
def chatbot_ai_response(request):
    start_time = time.time()
    user_input = request.POST.get('user_input', '').strip()
    if not user_input:
        return JsonResponse({'ai_response': "Please enter a message.", 'sentiment': user_sentiment}, status=400)
    user_sentiment = analyze_sentiment(user_input)

    cache_key = f"chatbot_response_{user_input}"
    cached_response = cache.get(cache_key)
    if cached_response:
        return JsonResponse({'ai_response': cached_response})

    user_input_lower = user_input.lower()

    if any(word in user_input_lower for word in ["therapist", "therapists", "recommend"]):
        therapists = get_cached_therapists()
        if therapists:
            recs = [f"{t.name} ({t.specialization}) - {t.location}. Call: {t.phone}" for t in therapists]
            response_text = "Here are some therapist recommendations:\n" + "\n".join(recs)
        else:
            response_text = "I'm sorry, I don't have any therapist recommendations at the moment."

    elif any(word in user_input_lower for word in ["hospital", "hospitals", "clinic"]):
        hospitals = get_cached_hospitals()
        if hospitals:
            recs = [f"{h.name} - {h.location}. Contact: {h.contact_info}" for h in hospitals]
            response_text = "Here are some hospitals you might consider:\n" + "\n".join(recs)
        else:
            response_text = "I'm sorry, I don't have any hospital recommendations at the moment."

    elif any(word in user_input_lower for word in ["video", "watch", "mental health video"]):
        videos = get_cached_videos()
        if videos:
            recs = [f"{v.title}: {v.description}\nWatch: {v.video_url}" for v in videos]
            response_text = "Here are some helpful videos:\n\n" + "\n\n".join(recs)
        else:
            response_text = "I'm sorry, I don't have any video recommendations at the moment."
    else:
        # ✅ Only generate the response once (intent matching or GPT-2 fallback)
        response_text = generate_response(user_input)

    if request.user.is_authenticated:
        today = timezone.now().date()
        session = ConversationSession.objects.filter(user=request.user, start_time__date=today).last()
        if not session:
            session_title = create_session_title(user_input)
            session = ConversationSession.objects.create(user=request.user, title=session_title)
        Conversation.objects.create(user=request.user, session=session, message=user_input, response=response_text)

    cache.set(cache_key, response_text, timeout=60)
    return JsonResponse({'ai_response': response_text})

def get_cached_therapists():
    therapists = cache.get('therapist_recommendations')
    if not therapists:
        therapists = list(Therapist.objects.only('name', 'specialization', 'location', 'phone'))
        cache.set('therapist_recommendations', therapists, timeout=3600)
    return random.sample(therapists, min(len(therapists), 4))

def get_cached_videos():
    videos = cache.get('video_recommendations')
    if not videos:
        videos = list(Video.objects.only('title', 'description', 'video_url'))
        cache.set('video_recommendations', videos, timeout=3600)
    return random.sample(videos, min(len(videos), 3))

def get_cached_hospitals():
    hospitals = cache.get('hospital_recommendations')
    if not hospitals:
        hospitals = list(Hospital.objects.only('name', 'location', 'contact_info'))
        cache.set('hospital_recommendations', hospitals, timeout=3600)
    if not hospitals:
        return []
    return random.sample(hospitals, min(len(hospitals), 3))

def custom_logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def load_session_view(request):
    session_id = request.GET.get("session_id")
    try:
        session = ConversationSession.objects.get(id=session_id, user=request.user)
        convs = Conversation.objects.filter(session=session).order_by('timestamp')
        messages_data = []
        for conv in convs:
            messages_data.append({"type": "user", "text": conv.message})
            messages_data.append({"type": "ai", "text": conv.response})
        return JsonResponse({"messages": messages_data})
    except ConversationSession.DoesNotExist:
        return JsonResponse({"error": "Session not found."}, status=404)

def get_recent_conversations(request):
    if request.user.is_authenticated:
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

@login_required
@csrf_exempt
@require_POST
def delete_session(request, session_id):
    
    if request.method == 'DELETE':
        try:
            session = ConversationSession.objects.get(id=session_id)
            Conversation.objects.filter(session=session).delete() 
            session.delete()
            return JsonResponse({'success': True})
        except ConversationSession.DoesNotExist:
            return JsonResponse({'error': 'Session not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)