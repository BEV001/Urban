from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import LoginForm, RegistrationForm

# Главная страница
def home(request):
    return render(request, 'auth_app/home.html')


# Session-based login
def session_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # Задаем backend
            login(request, user)
            return redirect('secure_page_session')
    else:
        form = LoginForm()
    return render(request, 'auth_app/session_login.html', {'form': form})

# Регистрация
def session_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('secure_page_session')
    else:
        form = RegistrationForm()

    return render(request, 'auth_app/session_register.html', {'form': form})

# Защищенная страница
@login_required
def secure_page_session(request):
    username = request.user.username
    return render(request, 'auth_app/secure_page_session.html', {'username': username})


def logout_session(request):
    logout(request)
    return redirect('home')  # Перенаправление на главную страницу или страницу входа

# OAuth Login
def oauth_login(request):
    return render(request, 'auth_app/oauth.html')


def secure_page(request):
    username = request.user.username
    return render(request, 'auth_app/secure_page.html', {'username': username})

def logout_oauth(request):
    logout(request)
    return redirect('home')  # Перенаправление на главную страницу или страницу входа

@api_view(['GET', 'POST'])
def jwt_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            refresh = RefreshToken.for_user(user)
            # токен в куки
            response = redirect('secure_page_jwt')
            response.set_cookie('access_token', str(refresh.access_token), httponly=True, secure=True)
            response.set_cookie('refresh_token', str(refresh), httponly=True, secure=True)
            return response

    else:
        form = LoginForm()

    return render(request, 'auth_app/jwt_login.html', {'form': form})

# Регистрация
@api_view(['GET', 'POST'])
def jwt_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Создаём токены
            refresh = RefreshToken.for_user(user)
            #Перенаправление
            response = redirect('secure_page_jwt')
            response.set_cookie('access_token',
                                str(refresh.access_token),
                                httponly=True)  # Устанавливает доступ к cookies только через HTTP протокол
                                #secure=True) #Токен будет отправляться только через HTTPS
            response.set_cookie('refresh_token', str(refresh),
                                httponly=True)
                               # secure=True)
            return response
    else:
        form = RegistrationForm()

    return render(request, 'auth_app/jwt_register.html', {'form': form})


@api_view(['GET'])
def secure_page_jwt(request):
    # Пользователь будет доступен на основе валидного JWT токена
    username = request.user.username
    return render(request, 'auth_app/secure_page_jwt.html', {'username': username})


@api_view(['GET', 'POST'])
def logout_jwt(request):
    response = redirect('home')  # Перенаправить на главную страницу или страницу входа
    # Удаляем токены из cookies
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response