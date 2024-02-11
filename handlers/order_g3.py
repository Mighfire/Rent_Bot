from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import G3
from keyboards import keyboard_number, keyboard_back

router1 = Router()


# HP 840G3
@router1.message(F.text.lower() == "хочу такой!", G3.model)
async def cmd_reply(message: Message, state: FSMContext):
    await state.update_data(model="#HPg3")
    await state.set_state(G3.dat)
    await message.answer("Напишите даты аренды, например, 14.02 - 18.02")


@router1.message(G3.dat)
async def form_comment(message: Message, state: FSMContext):
    await state.update_data(dat=message.text)
    await state.set_state(G3.delivery)
    await message.answer("Нужна ли вам доставка? Если да - напишите адрес доставки, если нет - напишите 'Нет'")


@router1.message(G3.delivery)
async def form_comment(message: Message, state: FSMContext):
    await state.update_data(delivery=message.text)
    await state.set_state(G3.number)
    await message.answer("Отправьте свой номер телефона по кнопке ниже", reply_markup=keyboard_number)


@router1.message(G3.number)
async def form_number(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await state.clear()
    await bot.send_message(-4101713526, f"@{message.from_user.username}: {data}")
    await message.answer("Спасибо, мы получили ваш запрос, ответим в ближайшее время!🙌", reply_markup=keyboard_back)
