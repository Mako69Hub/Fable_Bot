from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Register(StatesGroup):
    name = State()
    character_one = State()
    character_two = State()
    hero = State()
    setting = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('text1')

    await state.set_state(Register.name)
    await message.answer('Введите имя персонажа')
