import asyncio
import logging
import keyboards as kb
from handlers import order, catalog, arenda
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command


from config import TOKEN_API

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(TOKEN_API)
# Диспетчер
dp = Dispatcher()
dp.include_routers(order.router, catalog.router, arenda.router)


# Хэндлер на команду /start
@dp.message(Command("start", "menu"))
async def cmd_start(message: types.Message):
    await message.answer("<b>Добро пожаловать в наш бот!🤖</b>"
                         "Здесь вы можете ознакомиться с нашей техникой и оформить заказ! Нажмите кнопку 📖Каталог "
                         "для ознакомления с моделями ноутбуков, если вы не знаете какая модель вам нужна нажмите "
                         "кнопку ✏️Оформить заказ и напишите нам ваши пожелания!", reply_markup=kb.keyboard_main,
                         parse_mode="HTML")

@dp.message(F.text.lower() == "вернуться в меню")
async def back(message: types.Message):
    await message.answer("<b>Добро пожаловать в наш бот!🤖</b>"
                         "Здесь вы можете ознакомиться с нашей техникой и оформить заказ! Нажмите кнопку 📖Каталог "
                         "для ознакомления с моделями ноутбуков, если вы не знаете какая модель вам нужна нажмите "
                         "кнопку ✏️Оформить заказ и напишите нам ваши пожелания!", reply_markup=kb.keyboard_main, parse_mode="HTML")

@dp.message(F.text.lower() == "💻о нас")
async def about_us(message: types.Message):
    await message.answer("Пpeдлaгaем в крaткосрочную или долгoсpочную арeнду ноутбуки для oфиса, удалeнки, "
                         "кoмaндиpoвки, на мероприятие. Для физлиц (с небoльшим зaлогoм), для OОO, ИП - бeз зaлога. У "
                         "нас тoлько прoфеcсиoнaльные бизнеc ноутбуки. Вы имеете полный контроль - можете удалить "
                         "предустановленное ПО, установить любое другое ПО. Оформление как физлицо - по договору "
                         "аренды с паспортными данными и залогом. Размер залога зависит от ноутбука. Для юрлица залог "
                         "не требуется! Работаем официально. Предоставляем все необходимые документы, чеки.",
                         reply_markup=kb.keyboard_back)
    await message.answer("Работаем с 10 до 22, бот доступен круглосуточно Наш сайт: comp.rent, Позвонить нам: +74994040374")

@dp.message(F.photo)
async def image_uploader(message: types.Message):
    photo_data = message.photo[-1]
    await message.answer(f"{photo_data.file_id}")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())