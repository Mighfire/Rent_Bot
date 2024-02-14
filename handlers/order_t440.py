# Кнопка оформить заказ с каталога
from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import T440
from keyboards import keyboard_number, keyboard_back, remove_keyboard

router1 = Router()


# Lenovo T440
@router1.message(F.text.lower() == "хочу такой!", T440.model)
async def cmd_reply(message: Message, state: FSMContext):
    await state.update_data(model="#LenovoT440")
    await state.set_state(T440.dat)
    await message.answer("Напишите даты аренды и количество, например, 14.02 - 18.02, 1 ноутбук",reply_markup=remove_keyboard)


@router1.message(T440.dat)
async def form_comment(message: Message, state: FSMContext):
    await state.update_data(dat=message.text)
    await state.set_state(T440.delivery)
    await message.answer("Нужна ли вам доставка? Если да - напишите адрес доставки, если нет - напишите 'Нет'")


@router1.message(T440.delivery)
async def form_comment(message: Message, state: FSMContext):
    await state.update_data(delivery=message.text)
    await state.set_state(T440.number)
    await message.answer("Отправьте свой номер телефона по кнопке ниже", reply_markup=keyboard_number)


@router1.message(T440.number)
async def form_number(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(number=message.contact.phone_number)

    data = await state.get_data()
    await state.clear()
    formatted_text = []
    [
        formatted_text.append(f"{key}:{value}")
        for key, value in data.items()
    ]
    text = '\n'.join(formatted_text)
    await bot.send_message(-4101713526, f"@{message.from_user.username}: {text}")
    await message.answer("Спасибо, мы получили ваш запрос, ответим в ближайшее время!🙌", reply_markup=keyboard_back)
