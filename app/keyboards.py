from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'),
     KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты', request_contact=True)]
],
    resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')

main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])













