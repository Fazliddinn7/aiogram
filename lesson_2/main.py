import logging
import sys
from asyncio import run

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from functions import get_user_info, start_answer, shutdown_answer

dp = Dispatcher()


async def start():
    dp.startup.register(start_answer)
    dp.message.register(get_user_info)
    dp.shutdown.register(shutdown_answer)
    bot = Bot(token='7061245022:AAFgL4MH4BDhwkwGUri1JlD_cSsuLkUjp8g',
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    run(start())
