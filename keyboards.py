from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


keyboard_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О нас"),
         KeyboardButton(text="Каталог"),
         KeyboardButton(text="Оформить заказ")]
    ],
    resize_keyboard=True
)

keyboard_back = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вернуться в меню")]
    ],
    resize_keyboard=True
)