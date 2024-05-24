from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_feed_buttons = [
    [InlineKeyboardButton(text='📞Перезвоните мне', callback_data='callMe'), InlineKeyboardButton(text='📞Свяжитесь со мной в чат-боте', callback_data='callMeChat')],
    [InlineKeyboardButton(text='🔙Назад', callback_data='exit')]
]

start_feed_keyboard = InlineKeyboardMarkup(inline_keyboard=start_feed_buttons)
