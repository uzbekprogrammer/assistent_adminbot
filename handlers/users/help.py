from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from filters import IsPrivate
from keyboards.default import forhelp
from loader import dp


@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Yordam menyusiga xush kelibsiz!\nKerakli tugmani tanlang")
    
    await message.answer(text, reply_markup=forhelp)
