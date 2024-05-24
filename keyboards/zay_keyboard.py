from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_zay_buttons = [
    [InlineKeyboardButton(text='📛Оставить заявку', callback_data='zayavka'), InlineKeyboardButton(text='💡Поделиться предложением', callback_data='podelitsa')],
    [InlineKeyboardButton(text='🔙Назад', callback_data='exit')]
]

start_zay_keyboard = InlineKeyboardMarkup(inline_keyboard=start_zay_buttons)