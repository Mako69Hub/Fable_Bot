from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from info.text import DESCRIPTION_HERO, DESCRIPTION_SETTING, TEST_RESULT, TEST

router = Router()


class Register(StatesGroup):
    name = State()
    character_one = State()
    character_two = State()
    character_three = State()
    hero = State()
    setting = State()

class Setting(StatesGroup):
    setting = State()


async def check_result_test(message: Message, test: str) -> None:
    result_test = TEST_RESULT[test]
    if message.text not in result_test:
        await message.answer('Выберите ответ кнопками ниже', reply_markup=kb.reply_kb(result_test))
        return True
    return False


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('text1: для старта команда /fable')


@router.message(Command('fable'))
async def cmd_fable(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Напишите имя вашего героя 📝')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    if message.text == None:
        await message.answer('Напиши имя текстом')
        return

    await state.update_data(name=message.text)
    await state.set_state(Register.character_one)

    button_inline, url = TEST[0]
    await message.answer('Время пройти первый тест', reply_markup=kb.inline_test(button_inline, url))

    button_reply = TEST_RESULT['character_one']
    await message.answer('Выберите кнопками ваш результат', reply_markup=kb.reply_kb(button_reply))


@router.message(Register.character_one)
async def register_character_one(message: Message, state: FSMContext):
    if await check_result_test(message, 'character_one'):
        return

    await state.update_data(character_one=message.text)
    await state.set_state(Register.character_two)

    button_inline, url = TEST[1]
    await message.answer('Время пройти второй тест', reply_markup=kb.inline_test(button_inline, url))

    button_reply = TEST_RESULT['character_two']
    await message.answer('Выберите кнопками ваш результат', reply_markup=kb.reply_kb(button_reply))


@router.message(Register.character_two)
async def register_character_two(message: Message, state: FSMContext):
    if await check_result_test(message, 'character_two'):
        return

    await state.update_data(character_two=message.text)
    await state.set_state(Register.character_three)

    button_inline, url = TEST[2]
    await message.answer('Время пройти третий тест', reply_markup=kb.inline_test(button_inline, url))

    button_reply = TEST_RESULT['character_three']
    await message.answer('Выберите кнопками ваш результат', reply_markup=kb.reply_kb(button_reply))


@router.message(Register.character_three)
async def register_character_three(message: Message, state: FSMContext):
    if await check_result_test(message, 'character_three'):
        return

    await state.update_data(character_three=message.text)
    await state.set_state(Register.hero)

    button_inline, url = TEST[3]
    await message.answer('Колесо фортуны подскажет, что у вас будет за герой',
                         reply_markup=kb.inline_test(button_inline, url))

    button_reply = TEST_RESULT['hero']
    await message.answer('Выберите кнопками ваш результат', reply_markup=kb.reply_kb(button_reply))


@router.message(Register.hero)
async def register_hero(message: Message, state: FSMContext):
    if await check_result_test(message, 'hero'):
        return

    await state.update_data(hero=message.text)
    await state.set_state(Setting.setting)

    data = await state.get_data()
    print(data)

    await message.answer(f'Ваше имя: {data["name"]}\nВаш герой: {data["hero"]}\n{DESCRIPTION_HERO[data["hero"]]}\n'
                         f'Ваши черты личности: {data["character_one"]}, {data["character_two"]}, '
                         f'{data["character_three"]}')

    # await message.answer('Теперь выберем сеттинг сказки',
    #                      eply_markup=kb.reply_kb(TEST_RESULT['setting'], 1))


@router.message(F.text == 'Викторианская Англия (балы, рыцари, войны)')
async def cmd1(message: Message):
    await message.answer('text2')
    # if message.text in DESCRIPTION_SETTING.items():
    #     await state.set_state(Setting.processing_choice)
    #     await message.answer(DESCRIPTION_SETTING[message.text],
    #                          reply_markup=kb.reply_kb(TEST_RESULT['Выбрать Королевство', 'А можно посмотреть всех?']))
    # else:
    #     await message.answer('Теперь выберем сеттинг сказки кнопками',
    #                             reply_markup=kb.reply_kb(TEST_RESULT['setting'], 1)
    #     return
