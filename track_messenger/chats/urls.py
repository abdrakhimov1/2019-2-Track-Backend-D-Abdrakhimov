from chats.views import chat_list
from chats.views import chat_category
from django.urls import path

urlpatterns = [
        path('', chat_list, name='chat_list'),
        path('category/<int:pk>/',chat_category,  name = 'chat_category'),
        ]
