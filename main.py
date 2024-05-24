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
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


class StartForm(StatesGroup):
    phone = State()
    name = State()




@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer('☀️Доброго времени суток, бот создан, чтобы обрабатывать заявки и обращения пользователей. Чтобы воспользоваться этим, пришлите для начала Ваше Имя и Фамилию')
    await state.set_state(StartForm.name)



    # await message.answer('''
    # ✈️Добро пожаловать в главное меню чат-бота Управляющей компании "УЭР-ЮГ". Здесь Вы можете оставить заявку для управляющей компании или направить свое предложение по управлению домом.
    # Просто воспользуйтесь кнопками меню, чтобы взаимодействовать с функциями бота:
    # ''', reply_markup=start_keyboard)

@dp.message(StartForm.name)
async def name_handler(message: Message, state: FSMContext):
    print(message.text)
    await state.update_data(name=message.text)
    await message.answer('📞Теперь отправьте Ваш номер телефона через +7 следующим сообщением:')
    await state.set_state(StartForm.phone)
    print(await state.get_data())

@dp.message(StartForm.phone)
async def phone_handler(message: Message, state: FSMContext):
    print(message.text)
async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    dp.include_router(menu_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())