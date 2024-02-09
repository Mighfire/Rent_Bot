# Кнопка каталог
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards import keyboard_catalog, keyboard_order_from_catalog
from handlers import order_from_catalog


router = Router()
router.include_router(order_from_catalog.router1)

@router.message(F.text.lower() == "📖каталог")
async def catalog(message: Message):
    await message.answer('Выберите интересующую вас модель для более подробной информации!', reply_markup=keyboard_catalog)

@router.message(F.text.lower() == "14")
async def t440(message:Message):
    name = "t440"
    await message.answer_photo(photo="AgACAgIAAxkBAAIBLmXDkdWP3G7SRWrZEJySv09pHIqyAAIT1DEbqaYYSjw-GgABdqBrmQEAAwIAA3gAAzQE",caption='sdf', reply_markup=keyboard_order_from_catalog)
    return name
