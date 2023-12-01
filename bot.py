import asyncio
import logging
import keyboards as kb
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.enums.dice_emoji import DiceEmoji

from config import TOKEN_API

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(TOKEN_API)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start", "menu"))
async def cmd_start(message: types.Message):
    await message.answer("<b>Добро пожаловать в наш бот!🤖</b>"
                         "Здесь вы можете ознакомится с нашей техникой и оформить заказ!", reply_markup=kb.keyboard_main, parse_mode="HTML")

@dp.message(F.text.lower() == "вернуться в меню")
async def back(message: types.Message):
    await message.answer("<b>Добро пожаловать в наш бот!🤖</b>"
                         "Здесь вы можете ознакомится с нашей техникой и оформить заказ!", reply_markup=kb.keyboard_main, parse_mode="HTML")

@dp.message(F.text.lower() == "о нас")
async def about_us(message: types.Message):
    await message.answer("Мы отличная компания, даем технику в аренду👨‍💻!",reply_markup=kb.keyboard_back)


#@dp.message(Command("dice"))
#async def cmd_dice(message: types.Message, bot: Bot):
    #await bot.send_message(-4033454240, 'Text')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())