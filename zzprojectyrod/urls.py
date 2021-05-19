from django.contrib import admin
from django.urls import path, include
from .views import index, discord_login, redirect_after_login, profile, get_authenticated_user, profile_view, logout_view


urlpatterns = [
    path('', index, name='index'),
    path('auth/user/', get_authenticated_user, name='get_authenticated_user'),
    path('oauth2/login/', discord_login, name='oauth_login'),
    path('oauth2/login/profile/', profile, name='profile'),
    path('oauth2/login/redirect/', redirect_after_login, name='redirect_after_login'),
    path('profile/', profile_view, name='profile_view'),
    path('logout/', logout_view, name='logout'),

]