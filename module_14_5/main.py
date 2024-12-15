import os
import re

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

from keyboard import *
from config import *
import text
import logging
from crud_functions import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

def is_latin_only(text):
    return bool(re.fullmatch(r'^[a-zA-Z]+$', text))

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer(f"Добро пожаловать, {message.from_user.username}!", reply_markup=start_kb)

#MAIN MENU
@dp.message_handler(text="Рассчитать")
async def calculation(message):
    await message.answer("Выбирите, что хотели бы сделать:", reply_markup=main_menu)

@dp.message_handler(text="Информация")
async def info(message):
    await message.answer(text.message_about, reply_markup=start_kb)

@dp.message_handler(text='Назад')
async def to_back(message):
    await message.answer(text.message_about, reply_markup=start_kb)

#PRODUCTS AND BUYINGS
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    i = 0
    for image in os.listdir('products'):
        await message.answer(f"Название: {products[i][1]} | Описание: {products[i][2]} | Цена: {products[i][3]}")
        with open("products/"+image, "rb") as img:
            await message.answer_photo(photo=img)
        i+=1
    await message.answer(text.message_choosing, reply_markup=kb_product)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):

    await call.message.answer(text.sell)
    await call.answer()




#REGISTRATION
@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if message.text == 'Купить' or message.text == 'Рассчитать' or message.text == 'Информация' or message.text == 'Назад':
        await message.answer("Регистрация прервана.\nВозвращаемся в главное меню.",
                             reply_markup=start_kb)
        await state.finish()
        return

    try:
        user_name = str(message.text)
        if not is_latin_only(user_name):
            await message.answer('Пожалуйста,введите корректное имя пользователя  (только латинский алфавит!)')
        else:
            if is_included(user_name):
                await message.answer(f'Пользователь c именем {user_name} уже существует, введите другое имя:')
            else:
                await state.update_data(username=user_name)
                data_user = await state.get_data()
                await message.answer('Введите свой email:')
                await RegistrationState.email.set()
    except ValueError:
        await message.answer('Это не похоже на латинский алфавит! Пожалуйста, введите свой имя латинскими буквами')

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    if message.text == 'Купить' or message.text == 'Рассчитать' or message.text == 'Информация' or message.text == 'Назад':
        await message.answer("Регистрация прервана.\nВозвращаемся в главное меню.",
                             reply_markup=start_kb)
        await state.finish()
        return

    user_email = str(message.text)
    await state.update_data(email=user_email)
    data_user = await state.get_data()
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    if message.text == 'Купить' or message.text == 'Рассчитать' or message.text == 'Информация' or message.text == 'Назад':
        await message.answer("Регистрация прервана.\nВозвращаемся в главное меню.",
                             reply_markup=start_kb)
        await state.finish()
        return

    try:
        user_age = float(message.text)
        if 0 < user_age < 120:
            await state.update_data(age=user_age)
            data_user = await state.get_data()

            add_user(data_user['username'],data_user['email'],data_user['age'])
            await message.answer(f"{data_user['username']} успешно зарегистрирован!\nВозвращаемся в главное меню.",
                                 reply_markup=start_kb)

            await state.finish()
        else:
            await message.answer('Пожалуйста, введите корректный возраст (от 1 до 119 лет).')
    except ValueError:
        await message.answer('Это не похоже на число! Пожалуйста, введите свой возраст числом.')


#CALCULATIONS
@dp.message_handler(text='Формула расчёта')
async def get_formulas(message):
    await message.answer(text.formula_info, reply_markup=main_menu)


@dp.message_handler(text='Рассчитать норму калорий')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    if message.text == 'Назад':
        await message.answer("Возвращаемся в главное меню.",
                             reply_markup=start_kb)
        await state.finish()
        return
    if message.text == 'Формула расчёта':
        await message.answer(text.formula_info,
                             reply_markup=main_menu)
        await state.finish()
        return

    try:
        age = float(message.text)
        if 0 < age < 120:
            await state.update_data(age = age)
            data = await state.get_data()
            await message.answer('Введите свой рост (см):')
            await UserState.growth.set()
        else:
            await message.answer('Пожалуйста, введите корректный возраст (от 1 до 119 лет).')
    except ValueError:
        await message.answer('Это не похоже на число! Пожалуйста, введите свой возраст числом.')


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    if message.text == 'Назад':
        await message.answer("Возвращаемся в главное меню.",
                             reply_markup=start_kb)
        await state.finish()
        return
    if message.text == 'Формула расчёта':
        await message.answer(text.formula_info,
                             reply_markup=main_menu)
        await state.finish()
        return
    try:
        growth = float(message.text)
        if 0 < growth < 300:
            await state.update_data(growth = growth)
            data = await state.get_data()
            await message.answer('Введите свой вес (кг):')
            await UserState.weight.set()
        else:
            await message.answer('Пожалуйста, введите корректный рост (от 1 до 300 см).')
    except ValueError:
        await message.answer('Это не похоже на число! Пожалуйста, введите свой рост числом в см.')

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    if message.text == 'Назад':
        await message.answer("Возвращаемся в главное меню.",
                             reply_markup=start_kb)
        await state.finish()
        return
    if message.text == 'Формула расчёта':
        await message.answer(text.formula_info,
                             reply_markup=main_menu)
        await state.finish()
        return
    try:
        weight = float(message.text)
        if 0 < weight < 500:
            await state.update_data(weight = weight)
            data = await state.get_data()

            cal_calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
            await message.answer(f'Ваша норма калорий: {cal_calories}', reply_markup=start_kb)
            await state.finish()

        else:
            await message.answer('Пожалуйста, введите корректный вес (от 1 до 500 кг).')
    except ValueError:
            await message.answer('Это не похоже на число! Пожалуйста, введите свой вес числом в кг.')






@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
