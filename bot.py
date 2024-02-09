import asyncio
import logging
import keyboards as kb
from handlers import order, catalog
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command


from config import TOKEN_API

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(TOKEN_API)
# Диспетчер
dp = Dispatcher()
dp.include_routers(order.router, catalog.router)


# Хэндлер на команду /start
@dp.message(Command("start", "menu"))
async def cmd_start(message: types.Message):
    await message.answer("<b>Добро пожаловать в наш бот!🤖</b>"
                         "Здесь вы можете ознакомиться с нашей техникой и оформить заказ!", reply_markup=kb.keyboard_main, parse_mode="HTML")

@dp.message(F.text.lower() == "вернуться в меню")
async def back(message: types.Message):
    await message.answer("<b>Добро пожаловать в наш бот!🤖</b>"
                         "Здесь вы можете ознакомиться с нашей техникой и оформить заказ!", reply_markup=kb.keyboard_main, parse_mode="HTML")

@dp.message(F.text.lower() == "💻о нас")
async def about_us(message: types.Message):
    await message.answer("Мы отличная компания, даем технику в аренду👨‍💻!",reply_markup=kb.keyboard_back)

@dp.message(F.photo)
async def image_uploader(message: types.Message):
    photo_data = message.photo[-1]
    await message.answer(f"{photo_data}")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())