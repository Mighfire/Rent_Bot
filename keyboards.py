from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

keyboard_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О нас"),
         KeyboardButton(text="Каталог"),
         KeyboardButton(text="Оформить заказ")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

keyboard_back = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вернуться в меню")]
    ],
    resize_keyboard=True
)

keyboard_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отправить номер", request_contact=True)]
    ],
    resize_keyboard=True
)

keyboard_catalog = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="14 дюйм (Core i5, SSD) Lenovo ThinkPad T440"),
         KeyboardButton(text="Вернуться в меню")]
    ],
    resize_keyboard=True
)