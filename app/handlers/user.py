"""User Handler"""
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

user = Router()

user_list = []


class Form(StatesGroup):
    pass


# @connection
# async def create_user(name: str, email: str, number_phone: int, order: int,
#                       session=AsyncSession) -> int:

#     Создает нового пользователя с использованием ORM SQLAlchemy.

#     Аргументы:
#     - username: str - имя пользователя
#     - email: str - адрес электронной почты
#     - password: str - пароль пользователя
#     - session: AsyncSession - асинхронная сессия базы данных

#     Возвращает:
#     - int - идентификатор созданного пользователя

#     user_ = User(name=name, email=email,
#                  number_phone=number_phone, order=order)
#     session.add(user_)
#     await session.commit()
#     return user_.id


@user.message(CommandStart())
async def cmd_start(message: Message):
    """Start cmd

    Args:
        message (Message): message user
    """
    await message.answer(text='Привет', reply_markup=main)
