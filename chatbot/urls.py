from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.welcome_view, name='welcome'),  # NEW: set welcome as homepage
    path('chat/', views.chatbot_view, name='chatbot_view'),  # moved chatbot to /chat/
    path('response/', views.chatbot_ai_response, name='chatbot_ai_response'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.custom_logout_view, name='logout'),
    #path('chatbot/get_response/', views.get_response, name='get_response'),
    path('recent_conversations/', views.get_recent_conversations, name='recent_conversations'),
    path('load_session/', views.load_session_view, name='load_session'),
    path('delete_session/', views.delete_session, name='delete_session'),

   
    



    #path("activate/<uidb64>/<token>/", views.activate_account, name="activate_account"),
]
