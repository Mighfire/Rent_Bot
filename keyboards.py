from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

remove_keyboard = ReplyKeyboardRemove(
    remove_keyboard=True
)

keyboard_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💻О нас"),
         KeyboardButton(text="📖Каталог"),
         KeyboardButton(text="✏️Оформить заказ")],
         [KeyboardButton(text="Вопрос по действующей аренде")]
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
        [KeyboardButton(text="14 дюйм (Core i5, SSD) Lenovo ThinkPad T440")],
        [KeyboardButton(text="14 дюйм (FHD IPS, Core i5, SSD) HP Elitebook 840 g3")],
        [KeyboardButton(text="Вернуться в меню")]
    ],
    resize_keyboard=True
)

keyboard_order_from_catalog = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Хочу такой!")],
        [KeyboardButton(text='📖Каталог')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)



