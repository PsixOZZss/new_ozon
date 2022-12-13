from aiogram import Bot, Dispatcher, executor, types

import main

TOKEN = '1720133943:AAHJi1QDV-Bv0lFHXyZILvhGKl7jPEfEN00'

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='open')
async def start_cmd_handler(message: types.Message):
    await message.answer('Поехали')
    err = main.starting_bot()
    await message.answer(err)

    media = types.MediaGroup()
    media.attach_photo(types.InputFile(f'./screens/test.png'))
    await message.answer_media_group(media=media)


@dp.message_handler(commands='close')
async def start_cmd_handler(message: types.Message):
    main.close_browser()
    await message.answer('Браузер успешно закрыт')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
