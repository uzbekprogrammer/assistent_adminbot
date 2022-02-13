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