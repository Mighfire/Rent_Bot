from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):  # Стейты оформления заказа
    comment = State()
    delivery = State()
    number = State()


class T440(StatesGroup):  # Стейты оформления заказа
    model = State()
    dat = State()
    delivery = State()
    number = State()


class G3(StatesGroup):  # Стейты оформления заказа
    model = State()
    dat = State()
    delivery = State()
    number = State()

class arenda(StatesGroup):
    comment = State()
    number = State()
    question = State()