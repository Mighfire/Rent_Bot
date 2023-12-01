from aiogram import types

kb_main_menu = [
        [types.KeyboardButton(text="О нас")],
        [types.KeyboardButton(text="Каталог")],
        [types.KeyboardButton(text="Оформить заказ")]
    ]
kb_back = [
    [types.KeyboardButton(text="Вернуться в меню")]
]

keyboard_main = types.ReplyKeyboardMarkup(
    keyboard=kb_main_menu,
    resize_keyboard=True
)

keyboard_back = types.ReplyKeyboardMarkup(
    keyboard=kb_back,
    resize_keyboard=True
)