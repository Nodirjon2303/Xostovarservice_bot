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


def button_tulov_type():
    button = [
        [
            InlineKeyboardButton('Naqd pul', callback_data='naqd')
        ],
        [
            InlineKeyboardButton("Karta orqali", callback_data='karta')
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

def location_button():
    con_keyboard = KeyboardButton(text='Send location', request_location=True)
    button = ReplyKeyboardMarkup(
        [
            [con_keyboard]
        ], resize_keyboard=True
    )
    return button
