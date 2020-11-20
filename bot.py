import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import types
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def process_start_command(message: types.Message):
	await message.reply(" Hi!!! 👋 👋  \nWrite me /notify_me and digit in seconds  to enable notification  ⏰")

@dp.message_handler(commands = ['help'])
async def help_command(message: types.Message):
	await message.reply("Write me /notify_me to enable notification ⏰")


@dp.message_handler(commands=['notify_me'])
async def timer_handler(message: types.Message):


    time_string = message.get_args()
    
    # try to convert it to `int`
    try:
        time = int(time_string)
    except (ValueError, TypeError):
        return await message.answer("Please set a digit in seconds for timer. E.g.: /notify_me 5")

    # success! timer is set!
    await message.answer(f'Okay, let me remind you in {time} seconds')
    
    # sleeping
    await asyncio.sleep(time)

    await message.answer("It's time! ⏰⏰⏰")
	
if __name__ == '__main__':
	executor.start_polling(dp)

