from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    comment = State()
    number = State()