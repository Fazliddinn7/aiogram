import logging
import os
import sys

from aiogram import Bot, Dispatcher, types
from asyncio import run

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

BOT_TOKEN = os.getenv('TOKEN')

dp = Dispatcher()


@dp.startup()
async def start_answer(bot: Bot):
    await bot.send_message(6318392141, "Bot ishga tushdi ✅")


@dp.shutdown()
async def shutdown_answer(bot: Bot):
    await bot.send_message(6318392141, 'Bot ishdan to\'xtadi ❌')


@dp.message()
async def echo(msg: types.Message, bot: Bot):
    await msg.copy_to(chat_id=msg.chat.id)


async def start():
    bot = Bot('', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    run(start())
