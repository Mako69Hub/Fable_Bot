from info.text import STORY


def one(text):
    if text == STORY[0][0]:
        print('dfgvbfdvb')
        result = f'{STORY[3][1]}\n\n'
        button = []

        for i in range(4, 6):
            title, text = STORY[i]
            result += f'{title}\n{text}\n\n'
            button.append(title)
        return result, button

