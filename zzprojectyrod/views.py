from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
import requests
from django.contrib.auth.decorators import login_required
from .models import LicenseKeys
from django.contrib import messages

discord_oauth2_url = 'https://discord.com/api/oauth2/authorize?client_id=840350173393059910&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify'


@login_required(login_url="/oauth2/login")
def profile_view(request):
    if 'k' in request.POST:
        k = request.POST['k']
        print(k)
        keyinmodel = LicenseKeys.objects.filter(key=k)
        if len(keyinmodel) == 0:
            messages.error(request, "License not found.")
        else:
            messages.success(request, 'Product Key has already been activated')
    else:
        print('net zaprosa')
    return render(request, 'zzprojectyrod/profile.html')


def index(request):
    return render(request, 'zzprojectyrod/index1.html')


def discord_login(request):
    return redirect(discord_oauth2_url)


def profile(request):
    return JsonResponse({'msg': 'profile'})


def redirect_after_login(request):
    code = request.GET.get('code')
    user = exchange_code(code)
    discord_user = authenticate(request, user=user)
    discord_user = list(discord_user).pop()
    print(discord_user)
    login(request, discord_user)
    return redirect("/profile/")


def exchange_code(code):
    data = {
        "client_id": '840350173393059910',
        'client_secret': 'cJPzRhIK2830pYjGIjgm44f57e1Y3VUi',
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': "http://127.0.0.1:8000/oauth2/login/redirect",
        'scope': 'identify',
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        'Authorization': 'Bearer %s' % access_token
    })
    print(response)
    user = response.json()
    print(user)
    return user


@login_required(login_url="/oauth2/login")
def get_authenticated_user(request):
    user = request.user
    avatar_url = 'https://cdn.discordapp.com/avatars/' + str(user.id) + '/' + str(user.avatar)
    print(avatar_url)
    return JsonResponse({
        "id": user.id,
        "discord_tag": user.discord_tag,
        "avatar": user.avatar,
        "public_flags": user.public_flags,
        "flags": user.flags,
        "locale": user.locale,
        "mfa_enabled": user.mfa_enabled
        })


def logout_view(request):
    logout(request)
    return redirect('index')


