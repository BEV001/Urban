from django.contrib import admin
from .models import Game, Buyer

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')  # Отображение полей в списке
    search_fields = ('title',)  # Поиск по полю title
    list_filter = ('size', 'cost')  # Фильтрация по size и cost
    list_per_page = 20  # Ограничение количества записей до 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')  # Отображение полей в списке
    search_fields = ('name',)  # Поиск по полю name
    list_filter = ('balance', 'age')  # Фильтрация по balance и age
    list_per_page = 30  # Ограничение количества записей до 30
    readonly_fields = ('balance',)  # Поле balance доступно только для чтения
