import asyncio

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.enums.dice_emoji import DiceEmoji

import app.keyboards as kb
import app.validator as vd
from info.text import DESCRIPTION_HERO, DESCRIPTION_SETTING, TEST_RESULT, TEST, STORY, FOTO_PATH

router = Router()
print('Ебашь')


class Register(StatesGroup):
    name = State()
    character_one = State()
    character_two = State()
    character_three = State()
    hero = State()
    setting = State()


class Fable(StatesGroup):
    stage = State()
    current = State()


class Setting(StatesGroup):
    setting = State()
    answer_setting = State()


async def check_result_test(message: Message, test: str) -> bool:
    result_test = TEST_RESULT[test]
    if message.text not in result_test:
        await message.answer('Выберите ответ кнопками ниже', reply_markup=kb.reply_kb(result_test))
        return True
    return False


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(STORY[101], reply_markup=kb.reply_kb(['/fable']))

    photo_path = 'foto/home.jpg'
    await message.answer_photo(photo=FSInputFile(photo_path))


@router.message(Command('fable'))
async def cmd_fable(message: Message, state: FSMContext):
    await state.set_state(Register.name)

    await message.answer('Напишите имя вашего героя 📝')

    photo_path = 'foto/name.jpg'
    await message.answer_photo(photo=FSInputFile(photo_path))


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    if message.text == None or len(message.text) > 200:
        await message.answer('Напиши имя текстом! Не более 200 символов')
        return

    await state.update_data(name=message.text)
    await state.set_state(Register.character_one)

    photo_path = 'foto/character.jpg'
    await message.answer_photo(photo=FSInputFile(photo_path))

    button_inline, url = TEST[0]
    await message.answer('Время пройти первый тест "однажды в таверне" ↓, ', reply_markup=kb.inline_test(button_inline, url))

    await asyncio.sleep(5)
    button_reply = TEST_RESULT['character_one']
    await message.answer('Выберите кнопками ваш результат!', reply_markup=kb.reply_kb(button_reply),
                         disable_notification=True)


@router.message(Register.character_one)
async def register_character_one(message: Message, state: FSMContext):
    if await check_result_test(message, 'character_one'):
        return

    await state.update_data(character_one=message.text)
    await state.set_state(Register.character_two)

    photo_path = 'foto/character.jpg'
    await message.answer_photo(photo=FSInputFile(photo_path))

    button_inline, url = TEST[1]
    await message.answer('Время пройти второй тест "однажды на дороге" ↓', reply_markup=kb.inline_test(button_inline, url))

    await asyncio.sleep(5)
    button_reply = TEST_RESULT['character_two']
    await message.answer('Выберите кнопками ваш результат!', reply_markup=kb.reply_kb(button_reply),
                         disable_notification=True)


@router.message(Register.character_two)
async def register_character_two(message: Message, state: FSMContext):
    if await check_result_test(message, 'character_two'):
        return

    await state.update_data(character_two=message.text)
    await state.set_state(Register.character_three)

    photo_path = 'foto/character.jpg'
    await message.answer_photo(photo=FSInputFile(photo_path))

    button_inline, url = TEST[2]
    await message.answer('Время пройти третий тест "однажды дома" ↓', reply_markup=kb.inline_test(button_inline, url))

    await asyncio.sleep(5)
    button_reply = TEST_RESULT['character_three']
    await message.answer('Выберите кнопками ваш результат!', reply_markup=kb.reply_kb(button_reply),
                         disable_notification=True)


@router.message(Register.character_three)
async def register_character_three(message: Message, state: FSMContext):
    if await check_result_test(message, 'character_three'):
        return

    await state.update_data(character_three=message.text)
    await state.set_state(Register.hero)

    photo_path = 'foto/hero.jpg'
    await message.answer_photo(photo=FSInputFile(photo_path))

    button_inline, url = TEST[3]
    await message.answer('Колесо фортуны подскажет, что у вас будет за герой',
                         reply_markup=kb.inline_test(button_inline, url))

    await asyncio.sleep(5)
    button_reply = TEST_RESULT['hero']
    await message.answer('Выберите кнопками ваш результат!', reply_markup=kb.reply_kb(button_reply),
                         disable_notification=True)


@router.message(Register.hero)
async def register_hero(message: Message, state: FSMContext):
    if await check_result_test(message, 'hero'):
        return

    await state.update_data(hero=message.text)
    await state.set_state(Setting.setting)

    data = await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\nВаш персонаж: {data["hero"]}\n{DESCRIPTION_HERO[data["hero"]]}\n'
                         f'Ваши черты личности: {data["character_one"]}, {data["character_two"]}, '
                         f'{data["character_three"]}')

    await asyncio.sleep(4)
    photo_path = 'foto/kingdom.jpg'
    await message.answer_photo(photo=FSInputFile(photo_path))

    button_reply = TEST_RESULT['setting']
    await message.answer('Теперь выберем сеттинг сказки:', reply_markup=kb.reply_kb(button_reply, 1))


@router.message(Setting.setting)
async def setting(message: Message, state: FSMContext):
    if await check_result_test(message, 'setting'):
        return

    await state.update_data(setting=message.text)
    await state.set_state(Setting.answer_setting)

    description = DESCRIPTION_SETTING[message.text]
    button_reply = TEST_RESULT['answer_setting']
    await message.answer(description, reply_markup=kb.reply_kb(button_reply))

    photo_path = FOTO_PATH[message.text]
    await message.answer_photo(photo=FSInputFile(photo_path))


@router.message(Setting.answer_setting)
async def setting_answer(message: Message, state: FSMContext):
    if await check_result_test(message, 'answer_setting'):
        return

    yes, no = TEST_RESULT['answer_setting']
    if message.text == yes:
        await state.set_state(Fable.stage)
        await state.update_data(current=-1, stage=-1)
        await message.answer('А теперь давай писать сказку!')

        result, button_reply = vd.generation_msg(-1)
        await message.answer(result, reply_markup=kb.reply_kb(button_reply))

    else:
        await state.set_state(Setting.setting)
        button_reply = TEST_RESULT['setting']
        await message.answer('Выберите кнопками интересующий сеттинг:',
                             reply_markup=kb.reply_kb(button_reply, 1))


@router.message(Fable.stage)
async def fable_stage(message: Message, state: FSMContext):
    data_cur = await state.get_data()
    current = data_cur.get('current')  # текущий этап пользователя
    stage = data_cur.get('stage')  # Список всех состояний пользователя в истории

    if not vd.check_but_story(message.text, current):  # Проверка, нажал ли на кнопку
        button_reply = vd.generation_button(current)  # Генератор кнопок по текущему статусу пользователя
        await message.answer('Воспользуйтесь кнопками!', reply_markup=kb.reply_kb(button_reply))
        return

    number_cur_story = vd.num_story(message.text)  # По ответу получаем номер состояния


    if number_cur_story == 33:
        await message.answer('Вот и закончилась наша история. Вывожу ваш путь...')

        data = await state.get_data()
        await message.answer(
            f'✍️ Ваше имя: {data["name"]}\n👤Ваш персонаж: {data["hero"]}\n{DESCRIPTION_HERO[data["hero"]]}\n'
            f'🪬Ваши черты личности: {data["character_one"]}, {data["character_two"]}, '
            f'{data["character_three"]}')

        await message.answer(f'🏰Сеттинг сказки: {data["setting"]}\n{DESCRIPTION_SETTING[data["setting"]]}')

        story_end = vd.result_story(stage)
        for msg in story_end:
            await message.answer(msg)

        photo_path = FOTO_PATH['end']
        await message.answer_photo(photo=FSInputFile(photo_path))

        await asyncio.sleep(3)
        await message.answer('Мы создали скелет для вашей сказки. Теперь скопируйте его к себе и приступайте к написанию истории!📝')
        await state.clear()
        return

    elif number_cur_story == 32:
        await state.update_data(current=-1, stage=-1)

        result, button_reply = vd.generation_msg(-1)
        await message.answer(result, reply_markup=kb.reply_kb(button_reply))
        return

    elif number_cur_story in [21, 50, 53]:
        photo_path = FOTO_PATH['lose']
        await message.answer_photo(photo=FSInputFile(photo_path))

    elif number_cur_story in [20, 28]:
        photo_path = FOTO_PATH['win']
        await message.answer_photo(photo=FSInputFile(photo_path))


    await state.update_data(current=number_cur_story)  # Меняем текущее состояние

    new_stage = f'{stage}, {number_cur_story}'  # Дополняем общее состояние
    await state.update_data(stage=new_stage)  # Записываем общее состояние

    if number_cur_story == 15:
        result_dice = await message.answer_dice(DiceEmoji.DICE)
        result_dice = result_dice.dice.value

        result, new_num_story = vd.result_dice(number_cur_story, result_dice)
        button_reply = vd.generation_button(new_num_story)

        await asyncio.sleep(5)
        await message.answer(result, reply_markup=kb.reply_kb(button_reply))

        new_stage = f'{stage}, {new_num_story}'  # Дополняем общее состояние
        await state.update_data(stage=new_stage)  # Записываем общее состояние
        await state.update_data(current=new_num_story)
        return

    result, button_reply = vd.generation_msg(number_cur_story)
    await message.answer(result, reply_markup=kb.reply_kb(button_reply))
