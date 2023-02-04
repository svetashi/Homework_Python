from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
import datetime
from bot_log import log
import json, os

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

'''____________________________________________________'''

CONVO_END = ConversationHandler.END
FUNC_CHOICE, HEALTH, HEALTH_IN, HEALTH_OUT, PET, PET_IN, PET_OUT, BIRTHSDAYS,  BIRTHSDAYS_IN, BIRTHSDAYS_OUT, NOTES, NOTES_IN, NOTES_OUT = range(13)

if not os.path.exists('info.json'):
    with open('info.json', 'w') as file:
        info = {}
        info.setdefault('health', [])
        info.setdefault('pet', [])
        info.setdefault('birthsdays', [])
        info.setdefault('notes', [])
        file.write(json.dumps(info))

async def health_in_read(update, context):
    with open('info.json', 'r', encoding='utf-8') as file:
        info = json.loads(file.read())
    
    info['health'].append(update.message.text)
    
    with open('info.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(info))
    
    await log(update.message.from_user.id, 'health_in_read', f"message: {update.message.text}")
    await update.message.reply_text(f"I got: {update.message.text}")
    return CONVO_END

async def health_in(update):
    await log(update.from_user.id, "health_in", "writing text")
    await update.message.reply_text("введи дату и причину")
    return HEALTH_IN

async def health_out(update):
    with open('info.json', 'r', encoding='utf-8') as file:
        text = '\n'.join(json.loads(file.read())['health'])
    await log(update.from_user.id,"health_out", f"outputting: {text}")
    await update.message.reply_text(text)
    return CONVO_END

async def health(update):
    await log(update.from_user.id, 'health', 'choosing option')
    keyboard = [
        [
            InlineKeyboardButton("Ввести", callback_data="health_in"),
            InlineKeyboardButton("Вывести", callback_data="health_out")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)
    return FUNC_CHOICE

'''____________________________________________________'''

async def pet_in_read(update, context):
    with open('info.json', 'r', encoding='utf-8') as file:
        info = json.loads(file.read())
    
    info['pet'].append(update.message.text)
    
    with open('info.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(info))

    await log(update.message.from_user.id, 'pet_in_read', f"message: {update.message.text}")
    await update.message.reply_text(f"I got: {update.message.text}")
    return CONVO_END

async def pet_in(update):
    await log(update.from_user.id, "pet_in", "writing text")
    await update.message.reply_text("введи дату и причину")
    return PET_IN

async def pet_out(update):
    with open('info.json', 'r', encoding='utf-8') as file:
        text = '\n'.join(json.loads(file.read())['pet'])
    await log(update.from_user.id,"pet_out", f"outputting: {text}")
    await update.message.reply_text(text)
    return CONVO_END

async def pet(update):
    await log(update.from_user.id, 'pet', 'choosing option')
    keyboard = [
        [
            InlineKeyboardButton("Ввести", callback_data="pet_in"),
            InlineKeyboardButton("Вывести", callback_data="pet_out")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)
    return FUNC_CHOICE


'''____________________________________________________'''


async def birthsdays_in_read(update, context):
    with open('info.json', 'r', encoding='utf-8') as file:
        info = json.loads(file.read())
    
    info['birthsdays'].append(update.message.text)
    
    with open('info.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(info))

    await log(update.message.from_user.id, 'birthsdays_in_read', f"message: {update.message.text}")
    await update.message.reply_text(f"I got: {update.message.text}")
    return CONVO_END

async def birthsdays_in(update):
    await log(update.from_user.id, "birthsdays_in", "writing text")
    await update.message.reply_text("введи дату и имя")
    return BIRTHSDAYS_IN

async def birthsdays_out(update):
    with open('info.json', 'r', encoding='utf-8') as file:
        text = '\n'.join(json.loads(file.read())['birthsdays'])
    await log(update.from_user.id,"birthsdays_out", f"outputting: {text}")
    await update.message.reply_text(text)
    return CONVO_END

async def birthsdays(update):
    await log(update.from_user.id, 'birthsdays', 'choosing option')
    keyboard = [
        [
            InlineKeyboardButton("Ввести", callback_data="birthsdays_in"),
            InlineKeyboardButton("Вывести", callback_data="birthsdays_out")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)
    return FUNC_CHOICE


'''____________________________________________________'''


async def notes_in_read(update, context):
    with open('info.json', 'r', encoding='utf-8') as file:
        info = json.loads(file.read())
    
    info['notes'].append(update.message.text)
    
    with open('info.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(info))

    await log(update.message.from_user.id, 'notes_in_read', f"message: {update.message.text}")
    await update.message.reply_text(f"I got: {update.message.text}")
    return CONVO_END

async def notes_in(update):
    await log(update.from_user.id, "notes_in", "writing text")
    await update.message.reply_text("введи заметку")
    return NOTES_IN

async def notes_out(update):
    with open('info.json', 'r', encoding='utf-8') as file:
        text = '\n'.join(json.loads(file.read())['notes'])
    await log(update.from_user.id,"notes_out", f"outputting: {text}")
    await update.message.reply_text(text)
    return CONVO_END

async def notes(update):
    await log(update.from_user.id, 'notes', 'choosing option')
    keyboard = [
        [
            InlineKeyboardButton("Ввести", callback_data="notes_in"),
            InlineKeyboardButton("Вывести", callback_data="notes_out")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)
    return FUNC_CHOICE