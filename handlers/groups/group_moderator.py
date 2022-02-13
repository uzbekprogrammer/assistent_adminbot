"""

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
import asyncio
import datetime
import re
import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import Chat

from data.config import ADMINS
from filters import IsGroup, AdminFilter
from loader import dp, bot
# ----------------------------------------------------------------------------------------------------------------------
# /ro oki !ro (read-only) komandalari uchun handler
# foydalanuvchini read-only ya'ni faqat o'qish rejimiga o'tkazib qo'yamiz.


@dp.message_handler(IsGroup(), Command("mute", prefixes="!#$&/"), AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!mute|/mute) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5

    """
    !ro 
    !ro 5 
    !ro 5 test
    !ro test
    !ro test test test
    /ro 
    /ro 5 
    /ro 5 test
    /ro test
    """
    # 5-minutga izohsiz cheklash
    # !ro 5
    # command='!ro' time='5' comment=[]

    # 50 minutga izoh bilan cheklash
    # !ro 50 reklama uchun ban
    # command='!ro' time='50' comment=['reklama', 'uchun', 'ban']

    time = int(time)

    # Ban vaqtini hisoblaymiz (hozirgi vaqt + n minut)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
        await message.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Xatolik! {err.args}")
        return

    # Пишем в чат
    await message.answer(
        f"Foydalanuvchi {message.reply_to_message.from_user.full_name} {time} minut yozish huquqidan mahrum qilindi.\n"
        f"Sabab: \n<b>{comment}</b>")

    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")
    # 5 sekun kutib xabarlarni o'chirib tashlaymiz
    await asyncio.sleep(1)
    await message.delete()
    await service_message.delete()


# read-only holatdan qayta tiklaymiz
@dp.message_handler(IsGroup(), Command("unmute", prefixes="!#$&/"), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )
    service_message = await message.reply("Xabar 1 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(1)
    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f"Foydalanuvchi {member.full_name} tiklandi")

    # xabarlarni o'chiramiz
    await message.delete()
    await service_message.delete()


# Foydalanuvchini banga yuborish (guruhdan haydash)


@dp.message_handler(IsGroup(), Command("ban", prefixes="!#$&/"), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.kick(user_id=member_id)

    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} guruhdan haydaldi")
    service_message = await message.reply("Xabar 1 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(1)
    await message.delete()
    await service_message.delete()


# Foydalanuvchini bandan chiqarish, foydalanuvchini guruhga qo'sha olmaymiz (o'zi qo'shilishi mumkin)
@dp.message_handler(IsGroup(), Command("unban", prefixes="!#$&/"), AdminFilter())
async def unban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.unban(user_id=member_id)
    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} bandan chiqarildi")
    service_message = await message.reply("Xabar 1 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(1)

    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command("del", prefixes="!#$&/"), AdminFilter())
async def unban_user(message: types.Message):
    # member = message.reply_to_message.from_user

    # await asyncio.sleep(1)

    # await service_message.delete()
    await message.reply_to_message.delete()
    await message.delete()


@dp.message_handler(IsGroup(), Command('type', prefixes="!#$/"), AdminFilter())
async def type(message: types.Message):
    try:
        member = message.reply_to_message.from_user
    except:
        member = message.text
    # member_id = member.id
    # chat_id = message.chat.id
    command_parse = re.compile(r"(!type|/type) ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    comment = parsed.group(2)
    await message.delete()
    try:
        await message.reply_to_message.reply(comment)
    except:
        await message.answer(comment)


@dp.message_handler(IsGroup(), Command('reload', prefixes="/"), AdminFilter())
async def reload(msg: types.Message):
    chat_id = msg.chat.id
    chat_name = msg.chat.full_name
    message = f"Bot {chat_name} {chat_id} ga qoshildi"
    await bot.send_message(chat_id=ADMINS[0], text=message)

    await msg.reply(f"Assalomu aleykum <a href='t.me/admin'>Admin</a>.Bot qayta ishga tushdi ")


@dp.message_handler(IsGroup(), Command('info', prefixes="/"), AdminFilter())
async def info(msg: types.Message):
    member = msg.reply_to_message.from_user
    # print(Chat.get_administrators())
    await msg.answer(Chat.get_member(user_id=member.id))


# @dp.message_handler(IsGroup(), Command('count', prefixes="/"), AdminFilter())
# async def count(msg: types.Message):
#     print(Chat.get_member_count())


@dp.message_handler(IsGroup(), Command('admins', prefixes='!/'), AdminFilter())
async def admins(msg: types.Message):
    await msg.answer(bot.get_chat_administrators())


