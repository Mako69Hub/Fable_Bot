from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from info.text import TEST, TEST_RESULT


# main.kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='Button1'),
#             KeyboardButton(text='Button2')
#         ]
#     ],
#     resize_keyboard=True,
#     one_time_keyboard=True,
#     input_field_placeholder='Используйте кнопки'
# )
#
#
# links_kb = InlineKeyboardMarkup(
#     inline_keyboard=
# )


# def test_kb(question):
#     url = TEST[question]
#     print(url)
#
#     inline_keyboard = [
#         [
#             InlineKeyboardButton(text='Пройти тест', url=url)
#         ]
#     ]
#     return inline_keyboard
def inline_kb(test_num):
    url = TEST[test_num]

    links_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Пройти тест', url=url)
            ]
        ]
    )
    return links_kb


def reply_kb(text: str):
    builder = ReplyKeyboardBuilder()

    text = TEST_RESULT[text]

    [builder.button(text=txt) for txt in text]
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
