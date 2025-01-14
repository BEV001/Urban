from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

users = ["user1", "user_sample", "test_user"]


Title_web = "Task 5"
# Create your views here.
def sign_up_by_html(request):
    page_name = 'Форма регистрации'
    info = {}
    initial_data = {
        'username': '',
        'age': '',
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        initial_data = {
            'username': username,
            'age': age
        }

        errors = {}
        if username in users:
            errors['username'] = 'Пользователь уже существует'
        if password != repeat_password:
            errors['repeat_password'] = 'Пароли не совпадают'
        if int(age) < 18:
            errors['age'] = 'Вы должны быть старше 18'
        if errors:
            info['error'] = errors
        else:
            users.append(username)
            return HttpResponse(f"Приветствуем, {username}!")

    context = {
        'page_name': page_name,
        'Title_web': Title_web,
        'initial_data': initial_data,
        'info': info
    }
    return render(request, "fifth_task/registration_page.html", context)

def django_sign_up(request):
    page_name = 'Форма регистрации'
    info = {}
    initial_data = {
        'username': '',
        'age': '',
    }

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')

            initial_data = {
                'username': username,
                'age': age
            }

            errors = {}
            if username in users:
                errors['username'] = 'Пользователь уже существует'
            if password != repeat_password:
                errors['repeat_password'] = 'Пароли не совпадают'
            if int(age) < 18:
                errors['age'] = 'Вы должны быть старше 18'
            if errors:
                info['error'] = errors
            else:
                users.append(username)
                return HttpResponse(f"Приветствуем, {username}!")

    else:
        form = UserRegister(initial=initial_data)

    info['form'] = form

    context = {
        'page_name': page_name,
        'Title_web': Title_web,
        'initial_data': initial_data,
        'info': info
    }
    print('django_sign_up')
    return render(request, "fifth_task/registration_page.html", context)