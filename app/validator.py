from info.text import STORY


def generation_msg(result, ran):
    button = []
    for i in ran:
        title, text = STORY[i]
        result += f'{title}\n{text}\n\n'
        button.append(title)
    return result, button


def zero():
    result = ''
    button = []
    for i in range(3):
        title, text = STORY[i]
        result += f'{title}\n{text}\n\n'
        button.append(title)
    return result, button


def one(text):
    if text == STORY[0][0]:
        result = f'{STORY[3][1]}\n\n'
        result, button = generation_msg(result, range(4, 6))
        return result, button
    if text == STORY[1][0]:
        pass
        # ПОСРЕДНИЧЕСТВО

        # недостача

def two(text):
    if text == STORY[4][0]:
        result = STORY[6][1]
        return result # нарушить, что последует

    elif text == STORY[5][0]:
        pass  # подчиниться


# print(one('Отлучка 🚗'))
