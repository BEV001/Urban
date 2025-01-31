from django.shortcuts import render, redirect
from task_2.forms import UserRegister
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from task_2.models import Buyer, Game, News

#users = ["user1", "user_sample", "test_user"]


Title_web = "Task 2"
button_back = 'Вернуться обратно'
button_buy = 'Купить'
# Create your views here.

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
            if Buyer.objects.filter(name=username).exists():
                errors['username'] = 'Пользователь уже существует'
            if password != repeat_password:
                errors['repeat_password'] = 'Пароли не совпадают'
            #if int(age) < 18:
            #   errors['age'] = 'Вы должны быть старше 18'
            if errors:
                info['error'] = errors
            else:
                Buyer.objects.create(name=username, age=age)
                return redirect('platform')

    else:
        form = UserRegister(initial=initial_data)

    info['form'] = form

    context = {
        'page_name': page_name,
        'Title_web': Title_web,
        'initial_data': initial_data,
        'info': info
    }

    return render(request, "registration_page.html", context)

def platform(request):
    pagename = 'Главная страница'

    context = {
        'pagename': pagename,
    }

    return render(request, "platform.html", context)


def games(request):
    pagename = 'Игры'
    list_games = Game.objects.all().values('title', 'description', 'cost')

    context= {
        'pagename': pagename,
        'list_games': list_games,
        'button_back': button_back,
        'button_buy': button_buy
    }
    return render(request, "games.html", context)


def card(request):
    pagename = 'Корзина'
    info = 'Извините, ваша корзина пуста'
    context = {
        'pagename': pagename,
        'info': info,
        'button_back': button_back

    }
    return render(request, "card.html", context)


def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 2)  # Показываем 10 новостей на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news.html', {'news': page_obj})
