import time
import asyncio
from threading import Thread

from aiogram import Bot, Dispatcher, executor, types

from main import OzonManager

# поменять на свой токен
TOKEN = '1720133943:AAHJi1QDV-Bv0lFHXyZILvhGKl7jPEfEN00'

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

manager = OzonManager()
is_running = False


@dp.message_handler(commands='open')
async def start_cmd_handler(message: types.Message):
    global is_running
    if not is_running:
        th = Thread(target=between_callback, args=(message,))
        th.start()
        is_running = True
    await message.answer('Поехали')
    err = await manager.start(message, True)
    await message.answer(err)

    manager.screen()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile(f'./screens/test.png'))
    await message.answer_media_group(media=media)


@dp.message_handler(commands='run')
async def start_cmd_handler(message: types.Message):
    global is_running
    if not is_running:
        th = Thread(target=between_callback, args=(message,))
        th.start()
        is_running = True
    await message.answer('Поехали')
    err = await manager.start(message, False)
    await message.answer(err)

    manager.screen()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile(f'./screens/test.png'))
    await message.answer_media_group(media=media)


@dp.message_handler(commands='close')
async def start_cmd_handler(message: types.Message):
    manager.close_browser()
    await message.answer('Браузер успешно закрыт')


@dp.message_handler(commands='status')
async def start_cmd_handler(message: types.Message):
    manager.screen()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile(f'./screens/test.png'))
    await message.answer_media_group(media=media)


@dp.message_handler(commands='click')
async def start_cmd_handler(message: types.Message):
    manager.video_click()
    await message.answer('Клик')


async def check(message):
    while True:
        status = manager.get_status()
        if status == 'video':
            await message.answer('видео')
            await asyncio.sleep(20)
        else:
            await asyncio.sleep(1)


def between_callback(message):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(check(message))
    loop.close()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
