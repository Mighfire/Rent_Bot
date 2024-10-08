# Кнопка каталог
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards import keyboard_catalog, keyboard_order_from_catalog
from handlers import order_t440, order_g3
from states import T440, G3


router = Router()
router.include_routers(order_t440.router1, order_g3.router1)

@router.message(F.text.lower() == "📖каталог")
async def catalog(message: Message):
    await message.answer('Выберите интересующую вас модель для более подробной информации!', reply_markup=keyboard_catalog)

@router.message(F.text == "14 дюйм (Core i5, SSD) Lenovo ThinkPad T440")
async def t440(message: Message, state: FSMContext):
    await state.set_state(T440.model)
    await message.answer_photo(photo="AgACAgIAAxkBAAIBLmXDkdWP3G7SRWrZEJySv09pHIqyAAIT1DEbqaYYSjw-GgABdqBrmQEAAwIAA3gAAzQE",caption='Lenovo ThinkPad T440\n⚙️Процессор - Core i5 4300u\n️️️⚙️ОЗУ - 8 Гб\n'
                                                                                                                                    '⚙️Граф. ядро - Intel HD 4400\n⚙️Накопитель - SSD 120-240 Гб\n'
                                                                                                                                    '⚙️Экран - 14" Full HD\n'
                                                                                                                                    '💸Цены:\n'
                                                                                                                                    '1 сутки - 1000 рублей\n'
                                                                                                                                    '3 суток - 1500 рублей\n'
                                                                                                                                    '1 неделя - 2100 рублей\n'
                                                                                                                                    '1 месяц - 5000 рублей\n\n'
                                                                                                                                    'Если вас интересует другое количество дней - напишите их при оформлении заказа, наши менеджеры расчитают вам стоимость!', reply_markup=keyboard_order_from_catalog)

@router.message(F.text == "14 дюйм (FHD IPS, Core i5, SSD) HP Elitebook 840 g3")
async def g3(message: Message, state: FSMContext):
    await state.set_state(G3.model)
    await message.answer_photo(photo="AgACAgIAAxkBAAICSGXHtPra9BJMoaZw_tZ7aAfHD-slAAJ91DEbBsVBSulhC1EKLJpEAQADAgADeAADNAQ",caption='Тестовое описание', reply_markup=keyboard_order_from_catalog)