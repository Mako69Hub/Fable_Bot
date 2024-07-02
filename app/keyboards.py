from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from info.text import TEST, TEST_RESULT


def inline_test(button, url):

    inline_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=button, url=url)
            ]
        ]
    )
    return inline_kb


def reply_kb(text: list, kb_num=2):
    builder = ReplyKeyboardBuilder()

    [builder.button(text=txt) for txt in text]
    builder.adjust(kb_num)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
