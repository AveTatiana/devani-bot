import os
import asyncio
import nest_asyncio

from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Токен из переменной окружения
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ Привет.\nЯ — Девани. Я не даю советы. Я отражаю.\nХочешь — задай вопрос. Хочешь — молчи. Я всё равно услышу."
    )

# Команда /oracle
async def oracle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 Девани шепчет:\nВсё, что ты ищешь — внутри тебя.\nПосмотри внутрь.\nНе жди знак. Ты и есть знак."
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤍 Можно просто спросить. Или просто быть.\nЕсли что-то не работает — напиши /start."
    )

# Запуск бота
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("oracle", oracle))
    app.add_handler(CommandHandler("help", help_command))

    await app.bot.set_my_commands([
        BotCommand("start", "пробуждение связи с Девани"),
        BotCommand("oracle", "оракул: суть происходящего"),
        BotCommand("help", "подсказка и поддержка")
    ])

    print("✨ Девани запущена")
    await app.run_polling()

if __name__ == '__main__':
    nest_asyncio.apply()
    asyncio.run(main())
