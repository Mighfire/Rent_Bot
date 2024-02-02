from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):  # Стейты оформления заказа
    comment = State()
    number = State()
