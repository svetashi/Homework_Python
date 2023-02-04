from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from warnings import filterwarnings
from telegram.warnings import PTBUserWarning
from command import hi_command, FUNC_CHOICE,  health_in_read, health_in ,health_out, health,  HEALTH, HEALTH_IN, HEALTH_OUT, pet_in_read, pet_in, pet_out, pet, PET, PET_IN, PET_OUT, birthsdays_in_read, birthsdays_in, birthsdays_out, birthsdays, BIRTHSDAYS,  BIRTHSDAYS_IN, BIRTHSDAYS_OUT, notes_in_read, notes_in, notes_out, notes, NOTES, NOTES_IN, NOTES_OUT


filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Здоровье", callback_data="health"),
            InlineKeyboardButton("Дни рождения", callback_data="birthsdays")
        ],
        [
            InlineKeyboardButton("Питомец", callback_data="pet"),
            InlineKeyboardButton("Заметки", callback_data="notes")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)
    return FUNC_CHOICE


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await globals()[query.data](query)
    return globals()[query.data.upper()]

async def stop(update, context):
    pass


def main():
    application = ApplicationBuilder().token('5893580494:AAE3BYKV85HAp-h1oJYTUedwMc3o42iJ8vc').build()

    application.add_handler(ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states = {
            FUNC_CHOICE: [CallbackQueryHandler(button)],
            HEALTH: [CallbackQueryHandler(button)],
            HEALTH_IN: [MessageHandler(filters.TEXT, health_in_read)],
            HEALTH_OUT: [CallbackQueryHandler(button)],
            PET: [CallbackQueryHandler(button)],
            PET_IN: [MessageHandler(filters.TEXT, pet_in_read)],
            PET_OUT: [CallbackQueryHandler(button)],
            BIRTHSDAYS: [CallbackQueryHandler(button)],
            BIRTHSDAYS_IN: [MessageHandler(filters.TEXT, birthsdays_in_read)],
            BIRTHSDAYS_OUT: [CallbackQueryHandler(button)],
            NOTES: [CallbackQueryHandler(button)],
            NOTES_IN: [MessageHandler(filters.TEXT, notes_in_read)],
            NOTES_OUT: [CallbackQueryHandler(button)]
        },
        fallbacks=[CommandHandler('stop', stop), CommandHandler('start', start)],
        per_message=False
    ))


    application.add_handler(CommandHandler("hi", hi_command))

    application.run_polling()


if __name__=="__main__":
    main()
