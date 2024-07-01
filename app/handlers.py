from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.validator as vd
from info.text import DESCRIPTION_HERO, DESCRIPTION_SETTING, TEST_RESULT, TEST, STORY

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
    answer_setting = State()


async def check_result_test(message: Message, test: str) -> bool:
    result_test = TEST_RESULT[test]
    if message.text not in result_test:
        await message.answer('Выберите ответ кнопками ниже', reply_markup=kb.reply_kb(result_test))
        return True
    return False


async def check_result_story(message: Message, story: str) -> bool: #переписать проверку
    result_story = STORY[story]
    if message.text not in result_story:
        await message.answer('Выберите ответ кнопками ниже', reply_markup=kb.reply_kb(result_story))
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

    await message.answer(f'Ваше имя: {data["name"]}\nВаш герой: {data["hero"]}\n{DESCRIPTION_HERO[data["hero"]]}\n'
                         f'Ваши черты личности: {data["character_one"]}, {data["character_two"]}, '
                         f'{data["character_three"]}')

    button_reply = TEST_RESULT['setting']
    await message.answer('Теперь выберем сеттинг сказки', reply_markup=kb.reply_kb(button_reply, 1))


@router.message(Setting.setting)
async def setting(message: Message, state: FSMContext):
    if await check_result_test(message, 'setting'):
        return

    await state.update_data(setting=message.text)
    await state.set_state(Setting.answer_setting)

    description = DESCRIPTION_SETTING[message.text]
    button_reply = TEST_RESULT['answer_setting']
    await message.answer(description, reply_markup=kb.reply_kb(button_reply))


@router.message(Setting.answer_setting)
async def setting_answer(message: Message, state: FSMContext):
    if await check_result_test(message, 'answer_setting'):
        return

    yes, no = TEST_RESULT['answer_setting']
    if message.text == yes:
        await state.set_state(Fable.zero)
        await message.answer('Сохраняю...\nА теперь давай писать сказку\nВыберите один <b>зачин</b> вашей сказки')

        result = ''
        button_reply = []
        for i in range(3):
            title, text = STORY[i]
            result += f'{title}\n{text}\n\n'
            button_reply.append(title)

        await message.answer(result, reply_markup=kb.reply_kb(button_reply))

    else:
        await state.set_state(Setting.setting)
        button_reply = TEST_RESULT['setting']
        await message.answer('Выберите кнопками интересующий сеттинг',
                             reply_markup=kb.reply_kb(button_reply, 1))


class Fable(StatesGroup):
    zero = State()
    one = State()
    two = State()
    three = State()
    four = State()
    five = State()
    six = State()
    seven = State()
    eight = State()
    nine = State()
    ten = State()


@router.message(Fable.zero)
async def cls_zero(message: Message, state: FSMContext):

#Нужно бахнуть проверку
    await state.update_data(zero=message.text)
    await state.set_state(Fable.one)

    result, button_reply = vd.one(message.text)
    await message.answer(result, reply_markup=kb.reply_kb(button_reply))
