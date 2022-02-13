"""

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
import asyncio
import re

from aiogram import types
from aiogram.dispatcher.filters import Command

from data.config import ADMINS
from filters import IsPrivate
from keyboards.default import forhelp
from loader import dp, db, bot


@dp.message_handler(IsPrivate(), commands='start', user_id=ADMINS)
async def admin_hello(message: types.Message):
    await message.reply(f"Assalomu aleykum mening hukmdorim", reply_markup=forhelp)


@dp.message_handler(IsPrivate(), commands='allusers', user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    response = ''
    for user in users:
        response += f'{user}\n'
    await message.reply(response)


@dp.message_handler(IsPrivate(), commands="cleandatabase", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi")


@dp.message_handler(IsPrivate(), commands="rek", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    ketgan = []
    for user in users:
        user_id = user[0]
        # print(f"user_id{user}\nuser={user}\nADMINS={ADMINS}")
        try:
            await message.reply_to_message.copy_to(chat_id=user_id, reply_markup=message)
            ketgan.append(user_id)
        except:
            pass
        # await bot.send_message(chat_id=1361934966, text=msg)
        await asyncio.sleep(0.5)
    await bot.send_message(chat_id=1768033194, text=f"{ketgan}\n\n{len(ketgan)} ta userga yuborildi")


@dp.message_handler(IsPrivate(), commands="menu", user_id=ADMINS)
async def show_handlers(message: types.Message):
    await message.answer("<b>/allusers</b> - Hamma foydalanuvchilarni chiqaradi\n"
                         "<b>/rek</b> - Reklama uchun\n"
                         "<b>cleandatabase</b> - Ehtiyot boling\n"
                         "<b>!send</b> - ID raqam yozilgan odamga jonatildi\n"
                         "<b>!who</b> - ID raqamli odamni topib beradi\n")


@dp.message_handler(IsPrivate(), Command("who", prefixes='!#'), user_id=ADMINS)
async def search_user(message: types.Message):
    command_parse = re.compile(r"(!who|#who) ?(\d+)?")
    parsed = command_parse.match(message.text)
    user_id = int(parsed.group(2))
    users = db.select_all_users()
    for user in users:
        if user_id in user:
            await message.reply(f'<a href="tg://user?id={user_id}">{user[1]}</a> topildi.')
            break
    loop = await message.reply("Usernot found")
    await asyncio.sleep(5)
    await loop.delete()


@dp.message_handler(IsPrivate(), Command("send", prefixes='!#'), user_id=ADMINS)
async def search_user(message: types.Message):
    command_parse = re.compile(r"(!send|#send) ?(\d+)?")
    parsed = command_parse.match(message.text)
    user_id = int(parsed.group(2))
    try:
        await message.reply_to_message.copy_to(chat_id=user_id, reply_markup=message)
        await message.answer("Muvaffaqiyatli jonatildi")
    except:
        await message.answer("Jonatib bolmadi!\nUser botni blocklagan")
