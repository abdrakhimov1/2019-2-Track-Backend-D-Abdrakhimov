from django.urls import path
from django.urls import include
from users.views import index, profile_details, contacts_list, search_users
from django.contrib.auth import views

urlpatterns = [
    path('index', index, name='index'),
    path('profile/<int:pk>', profile_details, name='profile_details'),
    path('list', contacts_list, name='contacts_list'),
    path('search_users', search_users, name='search_users'),
]