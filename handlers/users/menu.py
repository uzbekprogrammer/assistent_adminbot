"""

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
from aiogram.types import Message

from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), text='💁🏻‍♂️Asosiy Buyruqlar')
async def show_main_menu(msg: Message):
    await msg.answer("""ASOSIY BUYRUQLAR

👮🏻 Admin va Moderatorlar uchun

👮🏻 /mute 5  foydalanuvchini 5 daqiqa Read Only rejimiga o'tkazadi (5 o'rniga istalgan son qoyasiz). U o'qiydi, ammo hech qanday xabar yubora olmaydi

👮🏻 /unmute ovozsiz holatidan chiqaradi

👮🏻 /ban sizga foydalanuvchini guruh havolasidan foydalanib qayta qo'shilish imkoniyatini bermasdan ban qilish imkonini beradi.

👮🏻 /unban foydalanuvchini guruhning qora ro'yxatidan o'chirishga imkon beradi, bu holatda ular guruhga yana qayta qo'shilishlari mumkin 

👮🏻 /info foydalanuvchi haqida ma'lumot beradi

👮🏻 /type bu funksiyadan keyin istalgan matn yozasiz va xabar bot tomonidan jo'natiladi

""")