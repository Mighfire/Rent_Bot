# Кнопка вопрос по действующей аренде
from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import arenda
from keyboards import keyboard_number, keyboard_back, remove_keyboard

router = Router()


@router.message(F.text.lower() == "вопрос по действующей аренде")
async def cmd_reply(message: Message, state: FSMContext):
    await state.set_state(arenda.comment)
    await message.answer("Напишите свой вопрос в свободной форме",reply_markup=remove_keyboard)


@router.message(arenda.comment)
async def form_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    await state.set_state(arenda.number)
    await message.answer("Отправьте свой номер телефона по кнопке ниже", reply_markup=keyboard_number)



@router.message(arenda.number)
async def form_number(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(number=message.contact.phone_number)
    await state.set_state(arenda.question)
    await state.update_data(question="Действующая аренда")
    data = await state.get_data()
    await state.clear()
    await bot.send_message(-4101713526, f"@{message.from_user.username}: {data}")
    await message.answer("Спасибо, мы получили ваш запрос, ответим в ближайшее время!🙌",reply_markup=keyboard_back)