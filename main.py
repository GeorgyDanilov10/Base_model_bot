"""Telegram survey bot"""
import asyncio
import logging
import os
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
from app.handlers.user import user


async def main():
    """main_function
    """
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(user)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
