import asyncio
import logging
import keyboards as kb
from handlers import order, catalog, arenda, obrat
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.client.session.aiohttp import AiohttpSession

from config import TOKEN_API

# session = AiohttpSession(proxy="http://proxy.server:3128")
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(TOKEN_API)  # ,session=session)
# Диспетчер
dp = Dispatcher()
dp.include_routers(order.router, catalog.router, arenda.router, obrat.router)


# Хэндлер на команду /start
@dp.message(Command("start", "menu"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать в бот компании CompRent!🤖\n"
                         "Здесь вы можете ознакомиться с нашей техникой и оформить заказ!\n\nНажмите кнопку 📖Каталог "
                         "для ознакомления с моделями ноутбуков.\n\nЕсли вы не знаете какая модель вам нужна - нажмите "
                         "кнопку ✏️Оформить заказ и напишите нам ваши пожелания!", reply_markup=kb.keyboard_main,
                         parse_mode="HTML")


@dp.message(F.text.lower() == "вернуться в меню")
async def back(message: types.Message):
    await message.answer("Добро пожаловать в бот компании CompRent!🤖\n"
                         "Здесь вы можете ознакомиться с нашей техникой и оформить заказ!\n\nНажмите кнопку 📖Каталог "
                         "для ознакомления с моделями ноутбуков.\n\nЕсли вы не знаете какая модель вам нужна - нажмите "
                         "кнопку ✏️Оформить заказ и напишите нам ваши пожелания!", reply_markup=kb.keyboard_main,
                         parse_mode='HTML')


@dp.message(F.text.lower() == "💻о нас")
async def about_us(message: types.Message):
    await message.answer("Пpeдлaгaем в крaткосрочную или долгoсpочную арeнду ноутбуки для oфиса, удалeнки, "
                         "кoмaндиpoвки, на мероприятие.\nДля физлиц (с небoльшим зaлогoм), для OОO, ИП - бeз зaлога.\nУ "
                         "нас тoлько прoфеcсиoнaльные бизнеc ноутбуки. Вы имеете полный контроль - можете удалить "
                         "предустановленное ПО, установить любое другое ПО.\nОформление как физлицо - по договору "
                         "аренды с паспортными данными и залогом. Размер залога зависит от ноутбука.Для юрлица залог "
                         "не требуется!\nРаботаем официально. Предоставляем все необходимые документы, чеки.",
                         reply_markup=kb.keyboard_back)
    await message.answer(
        "Работаем с 10:00 до 22:00\nБот доступен круглосуточно\nНаш сайт: comp.rent\nПозвонить нам: +74994040374")


@dp.message(F.photo)
async def image_uploader(message: types.Message):
    photo_data = message.photo[-1]
    await message.answer(f"{photo_data.file_id}")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
