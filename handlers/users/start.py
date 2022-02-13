"""

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from filters import IsPrivate
from loader import dp, db, bot


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    user_id = message.from_user.id
    # Foydalanuvchini bazaga qoshamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        count = db.count_users()[0]
        msg = f'<a href="tg://user?id={user_id}">{name}</a> bazaga qoshildi. \nBazada {count} ta foydalanuvchi bor.' \
              f'\nID {user_id}.'
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        # await bot.send_message(chat_id=ADMINS[0], text=err)
        pass
    await message.answer(f"""Assalomu alaykum {message.from_user.full_name}! 
Ushbu bot sizning guruhlaringizni oson va xavfsiz boshqarish uchun eng takomillashgan botdir! 
 
Botni guruhingizga qo'shing va ishga tushishi uchun admin huquqini bering!
 
QANDAY BUYRUQLAR BOR? 
Barcha buyruqlarni ko'rish va ular qanday ishlashini bilish uchun /help buyrug'ini yuboring!""")
