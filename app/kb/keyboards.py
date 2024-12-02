"""Menu user"""

from aiogram.types import KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

list_products = ['Nike', 'Adidas', 'Puma', 'Rebook']

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='basket'),
     InlineKeyboardButton(text='Создать пользователя',
                          callback_data='creat_user')
     ],],
    resize_keyboard=True,
    input_field_placeholder='Выберите меню',)


def prod():
    return list_products


async def catalog():
    keyboard = ReplyKeyboardBuilder()
    for product in list_products:
        keyboard.add(KeyboardButton(text=product))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)
