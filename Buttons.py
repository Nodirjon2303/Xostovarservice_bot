from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup
from db_helper import *


def main_buttons():
    buttons = ReplyKeyboardMarkup(
        [
            [
                '📝Buyurma qilish',
            ],
            [
                '☎️📞Biz bilan aloqa'
            ]
        ], resize_keyboard=True
    )
    return buttons


def button_photo():
    button = [
        [
            InlineKeyboardButton('HA', callback_data='ha')
        ],
        [
            InlineKeyboardButton("Yo'q", callback_data='yuq')
        ]
    ]
    return InlineKeyboardMarkup(button)


def task_button():
    buttons = [
        ['Ha✅'],
        ['⬅️Ortga']
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def phone_button():
    con_keyboard = KeyboardButton(text='Send Contact', request_contact=True)
    button = ReplyKeyboardMarkup(
        [
            [con_keyboard]
        ], resize_keyboard=True
    )
    return button


def mintaqa_buttons():
    regions = get_regions()
    buttons = []
    temp = []
    for i in regions:
        try:
            temp.append(InlineKeyboardButton(f'{i[0]}', callback_data=f'{i[0]}'))
        except Exception as e:
            print(e)
        if len(temp) == 2:
            buttons.append(temp)
            temp = []
    if len(temp) == 1:
        buttons.append(temp)
    return InlineKeyboardMarkup(buttons)
