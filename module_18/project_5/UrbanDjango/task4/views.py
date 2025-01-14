from django.shortcuts import render
from django.views.generic import TemplateView


button_back = 'Вернуться обратно'
button_buy = 'Купить'

# Create your views here.



def platform(request):
    pagename = 'Главная страница'

    context = {
        'pagename': pagename,
    }

    return render(request, "fourth_task/platform.html", context)


def games(request):
    pagename = 'Игры'
    list_games = [
        'Atomic Heart',
        'Cyberpank 2077',
        'PayDay 2']
    context= {
        'pagename': pagename,
        'list_games': list_games,
        'button_back': button_back,
        'button_buy': button_buy
    }
    return render(request, "fourth_task/games.html", context)


def card(request):
    pagename = 'Корзина'
    info = 'Извините, ваша корзина пуста'
    context = {
        'pagename': pagename,
        'info': info,
        'button_back': button_back

    }
    return render(request, "fourth_task/card.html", context)



from django.shortcuts import render

# Create your views here.
