from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import F
from aiogram.types import Message


BOT_TOKEN = '6954004997:AAFEOPlC3l2ebT_EdKiR9Z2UrSXpfwuR7CE'


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


async def process_ivt_command(message: Message):
    await message.answer(
        'Вы лучшие!'
    )


async def process_year_command(message: Message):
    await message.answer(
        'Сейчас апрель :)'
    )


async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступила фотография от {message.from_user.username}")


async def send_audio_echo(message: Message):
    print(message)
    await message.reply_audio(message.audio.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступило аудио-файл от {message.from_user.username}")


async def send_sticker_echo(message: Message):
    print(message)
    await message.reply_sticker(message.sticker.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступил стикер от {message.from_user.username}")


async def send_video_echo(message: Message):
    print(message)
    await message.reply_video(message.video.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступило видео от {message.from_user.username}")


async def send_document_echo(message: Message):
    print(message)
    await message.reply_document(message.document.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступил какой-то документ от {message.from_user.username}")


async def send_animation_echo(message: Message):
    print(message)
    await message.reply_animation(message.animation.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступила гифка от {message.from_user.username}")


async def send_voice_echo(message: Message):
    print(message)
    await message.reply_voice(message.voice.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступило голосовое сообщение от {message.from_user.username}")


async def send_echo(message: Message):
    print(message)
    await message.reply(text=message.text)


dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(process_ivt_command, Command(commands='ИВТ'))
dp.message.register(process_year_command, Command(commands='2024'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_document_echo, F.document)
dp.message.register(send_animation_echo, F.animation)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)