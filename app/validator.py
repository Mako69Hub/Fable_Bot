from info.text import STORY, HOOKUP


def generation_msg(cur):
    result = f"{STORY[cur]['message']}\n\n"
    button = []
    ran = HOOKUP[cur]
    for i in ran:
        title, text = STORY[i]['button'], STORY[i]['msg']
        result += f'{text}\n\n'
        button.append(title)
    return result, button


def generation_button(cur):
    button = []
    ran = HOOKUP[cur]

    for i in ran:
        button.append(STORY[i]['button'])
    return button


def num_story(text):
    for num, txt in STORY.items():
        if text in txt.values():
            return num


def result_story(stage):
    stg = stage.split(', ')
    story_us = []
    story = ''
    for choice in stg:

        # print(choice)
        story_cur = STORY[int(choice)]['message']

        if len(story+story_cur) > 4096:
            story_us.append(story)
            story = ''

        story = f'{story}\n\n{story_cur}'
    story_us.append(story)
    return story_us


def check_but_story(choice, cur_status):
    if choice in generation_button(cur_status):
        return True


def result_dice(cur, res_dice):
    if cur == 10:
        if res_dice in [1, 2]:
            return STORY[50]['message'], 50

        elif res_dice in [3, 4]:
            return STORY[51]['message'], 51

        else:
            return STORY[52]['message'], 52

    else:
        if res_dice in [1, 2]:
            return STORY[53]['message'], 53

        elif res_dice in [3, 4]:
            return STORY[54]['message'], 54

        else:
            return STORY[55]['message'], 55
