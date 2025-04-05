import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
FORWARD_CHAT_ID = -1002567506313  # ID твоей группы "Девани_чат"

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await context.bot.send_message(
            chat_id=FORWARD_CHAT_ID,
            text=f"{update.message.from_user.first_name}:\n{update.message.text}"
        )
        await update.message.reply_text("Я передам твой вопрос Татьяне.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, forward_message))
app.run_polling()
