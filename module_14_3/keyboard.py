from aiogram.types import *

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать норму калорий'),
         KeyboardButton(text='Формула расчёта')],
        [KeyboardButton(text='Купить')]
    ],
    resize_keyboard=True
)



kb_product = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Товар 1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Товар 2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Товар 3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Товар 4', callback_data='product_buying')]
    ],
    resize_keyboard=True
)
