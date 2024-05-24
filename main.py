import asyncio
import logging
import sys
from os import getenv
from handlers.menu_handler import router as menu_router
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN
from keyboards.start_keyboard import start_keyboard
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer('''
    ✈️Добро пожаловать в главное меню чат-бота Управляющей компании "УЭР-ЮГ". Здесь Вы можете оставить заявку для управляющей компании или направить свое предложение по управлению домом. 
    Просто воспользуйтесь кнопками меню, чтобы взаимодействовать с функциями бота:
    ''', reply_markup=start_keyboard)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    dp.include_router(menu_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())