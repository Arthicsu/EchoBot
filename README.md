# Программа "Интеллектуальные ответы от продвинутого ИИ" с использованием библиотеки __aiogram__

Программа нужна для получения от бота сообщения командами /start и /help или ответного сообщения (эхо) на любые виды сообщения. После первого ответа следует второй, который уже содержит ответ на все виды Ваших сообщений. <br />
Сделал студент ___группы ИВТ-101 Рощин Никита___

## Описание

Проект представляет собой простое консольное приложение, которое работает с __токеном телеграм бота__ и __библиотекой aiogram__.

## Установка
Прежде всего для корректной работы кода необходимо установить специальные библиотеки, которые описаны в файле ___"requirements.txt"___.
Соответственно:
1. Клонируйте репозиторий.
2. Устанавливаете все необходимые библиотеки (см. выше).

## Немного о важном

Реализовано через токен моего бота. Можете вставить токен своего бота, просто поменяйте значение:
```python
BOT_TOKEN = 'Ваш токен'
```
<br />

Пример кода хэндлера, который будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
```python
async def send_echo(message: Message):
    print(message)
    await message.reply(text=message.text)
```
Регистрируем хэндлеры
```python
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
```
## Использование

Запустите файл `main.py` и бот приобретёт небольшой "интеллект"  :)

