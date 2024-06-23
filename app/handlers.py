from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from info.text import DESCRIPTION
router = Router()


class Register(StatesGroup):
    name = State()
    character_one = State()
    character_two = State()
    character_three = State()
    hero = State()
    setting = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('text1')
    # await message.answer(DESCRIPTION['фантастика'])

    await state.set_state(Register.name)
    await message.answer('Введите имя персонажа')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(Register.character_one)
    await message.answer('Время пройти первый тест', reply_markup=kb.inline_kb('character_one'))

    await message.answer('Выберите кнопками ваш результат', reply_markup=kb.reply_kb('character_one'))


@router.message(Register.character_one)
async def register_character_one(message: Message, state: FSMContext):
    await state.update_data(character_one=message.text)

    await state.set_state(Register.character_two)
    await message.answer('Время пройти второй тест', reply_markup=kb.inline_kb('character_two'))

    await message.answer('Выберите кнопками ваш результат', reply_markup=kb.reply_kb('character_two'))


@router.message(Register.character_two)
async def register_character_two(message: Message, state: FSMContext):
    await state.update_data(character_two=message.text)

    await state.set_state(Register.character_three)
    await message.answer('Время пройти третий тест', reply_markup=kb.inline_kb('character_three'))

    await message.answer('Выберите кнопками ваш результат', reply_markup=kb.reply_kb('character_three'))


@router.message(Register.character_three)
async def register_character_three(message: Message, state: FSMContext):
    await state.update_data(character_three=message.text)

    await state.set_state(Register.hero)
    await message.answer('Колесо фортуны подскажет, что у вас будет за герой',
                         reply_markup=kb.inline_kb('hero'))

    await message.answer('Выберите кнопками ваш результат', reply_markup=kb.reply_kb('hero'))


@router.message(Register.hero)
async def register_hero(message: Message, state: FSMContext):
    await state.update_data(hero=message.text)

    data = await state.get_data()
    await state.clear()
    await message.answer(f'Ваше имя: {data["name"]}\nВаш герой: {data["hero"]}\nВаши черты личности: '
                         f'{data["character_one"]}, {data["character_two"]}, {data["character_three"]}')


# @router
#     await state.set_state(info_setting)



