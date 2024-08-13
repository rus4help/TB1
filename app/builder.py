from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

data = ('Nike', 'Adidas', 'Reebok')

def brands():
    keyboard = ReplyKeyboardBuilder()
    for brand in data:
        keyboard.add(KeyboardButton(text=brand))
    return keyboard.adjust(2).as_markup()