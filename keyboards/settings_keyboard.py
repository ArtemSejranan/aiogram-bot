from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_set_buttons = [
    [InlineKeyboardButton(text='🛠Поменять имя', callback_data='changeName'), InlineKeyboardButton(text='🛠Сменить номер', callback_data='changeNumber')],
    [InlineKeyboardButton(text='🔙Назад', callback_data='exit')]
]

start_set_keyboard = InlineKeyboardMarkup(inline_keyboard=start_set_buttons)