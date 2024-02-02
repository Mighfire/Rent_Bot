# Кнопка каталог
from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards import keyboard_catalog

router = Router()

@router.message(F.text.lower() == "каталог")
async def catalog(message: Message):
    await message.answer('Выберите интересующую вас модель для более подробной информации!', reply_markup=keyboard_catalog)

@router.message(F.text.lower() == "14 дюйм (Core i5, SSD) Lenovo ThinkPad T440")
async def t440(message:Message):
    await message.answer_photo()
