from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_buttons = [
    [InlineKeyboardButton(text='📛Оставить заявку', callback_data='zayavka'), InlineKeyboardButton(text='📞Связаться', callback_data='feedback')],
    [InlineKeyboardButton(text='⚙️Настройки', callback_data='settings')],
    [InlineKeyboardButton(text='☎️Полезные контакты', callback_data='contacts')]
]

start_keyboard = InlineKeyboardMarkup(inline_keyboard=start_buttons)