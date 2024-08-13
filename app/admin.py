from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

admim = Router()

@admim.message(Command('/adminpanel'))
async def cmd_apanel(message: Message):
    await message.answer('Это админ-панель.')