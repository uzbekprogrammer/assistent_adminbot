"""

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\nSiz guruhdasiz")
    await message.delete()
