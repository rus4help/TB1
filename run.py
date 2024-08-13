import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F

from app.handlers import router
from app.admin import admim


# Диспетчер следит за сообщениями, если ли какой-то запрос от пользователя
async def main():
    # Загрузка всего из файла .env
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(router, admim)
    await dp.start_polling(bot)

# Запуск данной функции доступен только из этого файла
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен.')