"""

Muallif: Mahmudov Abdurahim

http://t.me/BaDBoY_DeV

My portfolio: http://github.com/uzbekprogrammer

"""
from aiogram.types import Message

from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), text='ðð»ââï¸Asosiy Buyruqlar')
async def show_main_menu(msg: Message):
    await msg.answer("""ASOSIY BUYRUQLAR

ð®ð» Admin va Moderatorlar uchun

ð®ð» /mute 5  foydalanuvchini 5 daqiqa Read Only rejimiga o'tkazadi (5 o'rniga istalgan son qoyasiz). U o'qiydi, ammo hech qanday xabar yubora olmaydi

ð®ð» /unmute ovozsiz holatidan chiqaradi

ð®ð» /ban sizga foydalanuvchini guruh havolasidan foydalanib qayta qo'shilish imkoniyatini bermasdan ban qilish imkonini beradi.

ð®ð» /unban foydalanuvchini guruhning qora ro'yxatidan o'chirishga imkon beradi, bu holatda ular guruhga yana qayta qo'shilishlari mumkin 

ð®ð» /info foydalanuvchi haqida ma'lumot beradi

ð®ð» /type bu funksiyadan keyin istalgan matn yozasiz va xabar bot tomonidan jo'natiladi

""")