"""

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

forhelp = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🙇🏻Botni Sozlash Bo'yicha Qo'llanma🙇🏻"),
        ],
        [
            KeyboardButton(text='💁🏻‍♂️Asosiy Buyruqlar'),
            KeyboardButton(text='🙋🏻‍♂️Murakkab Buyruqlar')
        ],
    ],
    resize_keyboard=True
)