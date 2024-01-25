# Кнопка оформить заказ
from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import Form

router = Router()


@router.message(F.text.lower() == "оформить заказ")
async def cmd_reply(message: Message, state: FSMContext):
    await state.set_state(Form.comment)
    await message.answer("Напишите свой запрос")


@router.message(Form.comment)
async def form_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    await state.set_state(Form.number)
    await message.answer("Напишите свой номер телефона")


@router.message(Form.number)
async def form_number(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await state.clear()

    formatted_text = []
    [
        formatted_text.append(f"{key},{value}")
        for key, value in data.items()
    ]
    text = '\n'.join(formatted_text)
    await bot.send_message(-4033454240, f"@{message.from_user.username}: {text}")
