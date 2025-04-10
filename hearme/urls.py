from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_chatbot(request):
    return redirect('/chatbot/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')),
    path('', redirect_to_chatbot),  # Redirect root URL to chatbot
   

]
