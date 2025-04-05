import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
FORWARD_CHAT_ID = -1002567506313  # айди группы

# обработка обычного сообщения
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await context.bot.send_message(
            chat_id=FORWARD_CHAT_ID,
            text=f"{update.message.from_user.first_name}:\n{update.message.text}"
        )
        await update.message.reply_text("Я передам твой вопрос Татьяне.")

# обработка команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я рядом. Просто напиши.")

# обработка команды /oracle
async def oracle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔮 Девани шепчет:\nВсё, что ты ищешь — внутри тебя.")

# обработка команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Можно просто спросить. Или просто быть.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("oracle", oracle))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

app.run_polling()
