# Кнопка оформить заказ
from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import otziv
from keyboards import keyboard_back, remove_keyboard

router = Router()


@router.message(F.text.lower() == "оставить отзыв о боте")
async def cmd_reply(message: Message, state: FSMContext):
    await state.set_state(otziv.rating)
    await message.answer("Оцените бота от 1 до 10, где 1 - очень плохо, а 10 - все отлично.",reply_markup=remove_keyboard)

@router.message(otziv.rating)
async def cmd_reply(message: Message, state: FSMContext):
    await state.update_data(rating=message.text)
    await state.set_state(otziv.comment)
    await message.answer("Напишите почему вы поставили такую оценку, обратная связь очень важна для нас!",reply_markup=remove_keyboard)

@router.message(otziv.comment)
async def form_number(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(comment=message.text)
    await state.set_state(otziv.caption)
    await state.update_data(caption="#Отзывы")
    data = await state.get_data()
    await state.clear()
    formatted_text = []
    [
        formatted_text.append(f"{key}:{value}")
        for key, value in data.items()
    ]
    text = '\n'.join(formatted_text)
    await bot.send_message(-4101713526, f"@{message.from_user.username}: {text}")
    await message.answer("Спасибо за обратную связь! Благодаря вам мы становимся лучше!❤️",reply_markup=keyboard_back)