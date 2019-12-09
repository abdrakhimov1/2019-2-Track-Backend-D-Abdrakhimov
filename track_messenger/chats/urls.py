from django.urls import path
from django.urls import include
from chats.views import index, chat_detail, chat_page, chat_list, user_chat_list, create_personal_chat, send_message, chat_messages_list, read_message, upload_file

urlpatterns = [
    path('index', index, name='index'),
    path('detail/<int:pk>', chat_detail, name='chat_detail'),
    path('chat/<int:chat_id>', chat_page, name='chat_page'),
    path('list', chat_list, name='chat_list'),
    path('list_chats', user_chat_list, name='user_chat_list'),
    path('create_pers_chat', create_personal_chat, name='create_personal_chat'),
    path('send_msg', send_message, name='send_message'),
    path('chat_msg_list', chat_messages_list, name='chat_messages_list'),
    path('read_msg', read_message, name="read_message"),
    path('upload', upload_file, name="upload_file"),
]   