from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):  # Стейты оформления заказа
    comment = State()
    number = State()

class Form1(StatesGroup):  # Стейты оформления заказа
    model = State()
    data = State()
    number = State()
