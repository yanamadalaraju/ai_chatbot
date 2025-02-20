from django.urls import path
from .views import chat, chat_page
from chatbot import views


urlpatterns = [
    path("chat/",views.chat, name="chat"),
    path("",views.chat_page, name="chat_page"),  # Add frontend route
    # path("translate/", views.translate_text, name="translate"),
    # path("home/", views.translation_page, name="home"),
    path("api/chat/", chat, name="chat"),
    path("", chat_page, name="chat_page"),
]

