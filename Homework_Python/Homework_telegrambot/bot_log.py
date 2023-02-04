from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def log(user_id, function, message) -> None:
    file = open('log.txt', 'a', encoding='utf-8')
    file.write(f'{str(datetime.datetime.now())} - {user_id} - {function} - {message}\n')
    file.close()
