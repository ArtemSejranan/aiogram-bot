from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_contact_buttons = [
    [InlineKeyboardButton(text='🔙Назад', callback_data='exit')]
]

start_contact_keyboard = InlineKeyboardMarkup(inline_keyboard=start_contact_buttons)