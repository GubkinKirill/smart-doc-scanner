import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv
import os
from aiogram import types


load_dotenv()
BOT_TOKEN=os.getenv('BOT_TOKEN')

dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    text = 'Привет!Меня зовут DocVisionBot, я бот который поможет тебе отсканировать документ, получить текст с этого документа.'
    await message.answer(text=text)

@dp.message(Command('help'))
async def  handle_help(message: types.Message):
    await message.answer(text='Пришли мне фото документа и я сделаю тебе скан')

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())