from django.shortcuts import render
from django.views.generic import TemplateView

title_page = 'Task 3'
button_back = 'Вернуться обратно'
button_buy = 'Купить'

# Create your views here.
def platform(request):
    title = 'Главная страница'
    url_1 = 'Главная'
    url_2 = 'Магазин'
    url_3 = 'Корзина'
    context = {
        'title_page':  title_page,
        'title': title,
        'url_1': url_1,
        'url_2': url_2,
        'url_3': url_3,

    }

    return render(request, "third_task/platform.html", context)


def games(request):
    title = 'Игры'
    firts_games = 'Atomic Heart'
    second_game = 'Cyberpank 2077'
    third_game = 'PayDay 2'
    context= {
        'title_page':  title_page,
        'title': title,
        'firts_games': firts_games,
        'second_game': second_game,
        'third_game': third_game,
        'button_back': button_back,
        'button_buy': button_buy
    }
    return render(request, "third_task/games.html", context)


def card(request):
    title = 'Корзина'
    info = 'Извините, ваша корзина пуста'
    context = {
        'title_page': title_page,
        'title': title,
        'info': info,
        'button_back': button_back

    }
    return render(request, "third_task/card.html", context)



