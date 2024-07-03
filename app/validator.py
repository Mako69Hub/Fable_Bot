from info.text import STORY, HOOKUP


def generation_msg(cur):
    result = ''
    button = []
    ran = HOOKUP[cur]
    for i in ran:
        title, text = STORY[i]
        result += f'{title}\n{text}\n\n'
        button.append(title)
    return result, button


def generation_button(cur):
    button = []
    ran = HOOKUP[cur]
    # print(ran)
    for i in ran:
        button.append(STORY[i][0])
    # print('generation_button', button)
    return button


def num_story(text):
    for num, txt in STORY.items():
        if text in txt:
            return num





def check_but_story(choice, cur_status):
    if choice in generation_button(cur_status):
        return True

    #
    #     result, button_reply = vd.zero()
    #     # if await check_result_story(message, button_reply):
    #     result_test = TEST_RESULT[test]
    #     if message.text not in result_test:
    #         await message.answer('Выберите ответ кнопками ниже', reply_markup=kb.reply_kb(result_test))
    #         return True
    #     return False
    #
    # async def check_result_story(message: Message, button_reply) -> bool:  # переписать проверку\
    #     if message.text not in button_reply:
    #         await message.answer('Выберите ответ кнопками ниже', reply_markup=kb.reply_kb(button_reply))
    #         return True
    #     return False


def two(text):
    if text == STORY[0][0]:  # Если Отлучка
        result = f'{STORY[3][1]}\n\n'
        return generation_msg(result, range(4, 6))  # Нарушение или послушание

    if text == STORY[1][0]:
        pass
        # ПОСРЕДНИЧЕСТВО

        # недостача


def three(text):
    if text == STORY[5][0]:  # Послушаться
        result = f'{STORY[5][1]}\n\n'
        print(result)
        return generation_msg(result, range(1, 3))

    if text == STORY[4][0]:
        result = STORY[6][1]
        return result  # нарушить, что последует

    elif text == STORY[5][0]:
        pass  # подчиниться

# print(one())
# x = check_answer_story('Отлучка 🚗', -1)
# print(x)
generation_button(-1)