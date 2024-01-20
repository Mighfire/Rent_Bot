from aiogram import Router, F, Bot
from aiogram.types import Message

router = Router()


@router.message(F.text.lower() == "оформить заказ")
async def cmd_reply(message: Message):
    await message.answer("Напишите свой запрос")


@router.message(F.text.lower())
async def answer(message: Message, bot: Bot):
    await bot.send_message(-4033454240, '@' + message.from_user.username + ' ' + message.text)
