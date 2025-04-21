from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to Django's built-in User model
    fullname = models.CharField(max_length = 100, default="N/A")
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class ConversationSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, help_text="AI-generated title summary of the conversation")
    start_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.start_time.strftime('%Y-%m-%d')})"

class Conversation(models.Model):
    # Link each conversation message to its session:
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    session = models.ForeignKey(ConversationSession, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()  # User's message
    response = models.TextField()  # Chatbot's response
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation from {self.timestamp.strftime('%Y-%m-%d %H:%M')} (Session: {self.session.title if self.session else 'N/A'})"

# Your other models (Therapist, Video, etc.) remain unchanged.

class Therapist(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_url = models.URLField(help_text="URL to the video (e.g., a YouTube link)")

    def __str__(self):
        return self.title


