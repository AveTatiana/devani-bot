import os
import nest_asyncio
import asyncio
from telegram import Update, BotCommand
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
FORWARD_CHAT_ID = -1002567506313  # ID группы "Девани_чат"

# --- Команды ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ Привет.\nЯ — Девани. Я не даю советы. Я отражаю.\nХочешь — задай вопрос. Хочешь — молчи. Я всё равно услышу."
    )

async def oracle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 Девани шепчет:\nВсё, что ты ищешь — внутри тебя.\nПосмотри внутрь.\nНе жди знак. Ты и есть знак."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤍 Можно просто спросить. Или просто быть.\nЕсли что-то не работает — напиши /start."
    )

# --- Пересылка обычных сообщений ---
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await context.bot.send_message(
            chat_id=FORWARD_CHAT_ID,
            text=f"{update.message.from_user.first_name}:\n{update.message.text}"
        )
        await update.message.reply_text("Я передам твой вопрос Татьяне.")

# --- Запуск бота ---
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("oracle", oracle))
    app.add_handler(CommandHandler("help", help_command))

    # Обычные сообщения
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    # Меню команд
    await app.bot.set_my_commands([
        BotCommand("start", "пробуждение связи с Девани"),
        BotCommand("oracle", "оракул: суть происходящего"),
        BotCommand("help", "подсказка и поддержка")
    ])

    print("✨ Девани запущена через Webhook")
    await app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url=WEBHOOK_URL
    )

if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.run(main())
