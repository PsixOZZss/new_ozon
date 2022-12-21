import asyncio

from aiogram import Bot, Dispatcher, executor, types

from main import OzonManager

# поменять на свой токен
TOKEN = ''

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

manager = OzonManager()


@dp.message_handler(commands='open')
async def start_cmd_handler(message: types.Message):
    await message.answer('Поехали')
    err = await manager.start(message, True)
    await message.answer(err)

    manager.screen()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile(f'./screens/test.png'))
    await message.answer_media_group(media=media)


@dp.message_handler(commands='run')
async def start_cmd_handler(message: types.Message):
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
