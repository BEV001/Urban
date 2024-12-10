import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

from keyboard import *
from config import *
import text
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer(f"Добро пожаловать, {message.from_user.username}. "+text.message_about, reply_markup=start_kb)


@dp.message_handler(text="Купить")
async def add_menu(message):
    i = 1
    for image in os.listdir('products'):
        with open("products/"+image, "rb") as img:
            await message.answer_photo(img,f"Название: Товар {i} | Описание: описание {i} | Цена: {i*100}" )
        i+=1
    await message.answer(text.message_choosing, reply_markup=kb_product)

@dp.message_handler(text="Формула расчёта")
async def get_formulas(message):
    await message.answer(text.formula_info, reply_markup=start_kb)

@dp.message_handler(text="Рассчитать норму калорий")
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = float(message.text))
    data = await state.get_data()
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = float(message.text))
    data = await state.get_data()
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = float(message.text))
    data = await state.get_data()

    cal_calories = 10*data['weight']+6.25*data['growth']-5*data['age']+5
    await message.answer(f'Ваша норма калорий: {cal_calories}', reply_markup=start_kb)
    await state.finish()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(text.sell)
    await call.answer()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
