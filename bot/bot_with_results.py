import asyncio
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from telegram import Bot


bot_token = ""

chat_id = "219512885"

# Создаем объект Telegram бота
bot = Bot(token=bot_token)

# Создаем класс-обработчик событий файловой системы
class FileModifiedHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.txt'):
            # Читаем данные из файла
            with open(event.src_path, 'r') as file:
                data = file.read()

            # Отправляем данные в Telegram
            asyncio.create_task(send_message_to_telegram(chat_id, data))

# Указываем путь к отслеживаемой директории
path = 'C:\\Users\\anche\\PycharmProject\\Misis_po\\misis_po_kabanova\\reposts'

# Создаем объект отслеживания изменений в директории
event_handler = FileModifiedHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=False)


async def send_message_to_telegram(chat_id, data):
    # Отправляем данные в Telegram
    await bot.send_message(chat_id=chat_id, text=data)


async def main():
    # Запускаем отслеживание
    observer.start()

    try:
        # Пока отслеживание работает, продолжаем выполнение
        while observer.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        # Останавливаем отслеживание по нажатию Ctrl+C
        observer.stop()

    # Ожидаем завершения отслеживания
    observer.join()

# Запуск асинхронной функции main
asyncio.run(main())






