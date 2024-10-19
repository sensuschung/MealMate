from django.shortcuts import render
from forum.views import base_view

def home_view(request):
    message_reminder_visible = base_view(request)
    return render(request, 'homepage.html',{'message_reminder_visible': message_reminder_visible,})
