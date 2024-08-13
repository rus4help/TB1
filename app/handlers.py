import asyncio

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import app.keyboards as kb
import app.builder as builder

class Reg(StatesGroup):
    name = State()
    number = State()
    photo = State()

router = Router()

# Функция для обработки команды /start
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer(f'Привет! Введи своё имя')
#     await message.bot.send_chat_action(chat_id=message.from_user.id,
#                                        action=ChatAction.TYPING)
#     # await asyncio.sleep(2)
#     await message.reply(text='Привет!', reply_markup=builder.brands())
#     await message.answer('Купить VIP: /vip')

@router.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Отправь свой номер телефона')

@router.message(Reg.number)
async def reg_number(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(Reg.photo)
    await message.answer('Отправь своё фото')

@router.message(Reg.photo, F.photo)
async def reg_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    await message.answer_photo(photo=data['photo'], caption=f'Информация о Вас: {data['name']}, {data['number']}')
    await state.clear()

@router.callback_query(F.data == 'catalog')
async def cmd_catalog(callback: CallbackQuery):
    await callback.answer('Это каталог.', show_alert=True)
    await callback.message.answer('Вы открыли каталог.')


# Своя кастомная команда
@router.message(Command('vip'))
async def cmd_vip(message: Message):
    await message.answer(f'{message.from_user.username}, вы хотели купить VIP доступ?')

# Функция для обработки текстовых сообщений
@router.message(F.text == 'привет')
async def echo(message: Message):
    await message.reply('привет!!!')
    await message.answer(f'Ваш ID: {message.from_user.id}')

@router.message(F.photo)
async def echo(message: Message):
    photo_id = message.photo[-1].file_id
    await message.answer_photo(photo=photo_id)

@router.message(F.document)
async def echo(message: Message):
    await message.answer_document(document=message.document.file_id)

@router.message(F.audio)
async def echo(message: Message):
    await message.answer_audio(audio=message.audio.file_id)

@router.message(F.animation)
async def echo(message: Message):
    await message.answer_animation(animation=message.animation.file_id)
    await message.answer('Вы прислали гифку.')

@router.message(F.from_user.id == 779071751)
async def echo(message: Message):
    await message.answer(f'Написал определённый юзер с ID {message.from_user.id}')