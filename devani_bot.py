import os
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import nest_asyncio
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
FORWARD_CHAT_ID = -1002567506313  # ID твоей группы

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await context.bot.send_message(
            chat_id=FORWARD_CHAT_ID,
            text=f"{update.message.from_user.first_name}:\n{update.message.text}"
        )
        await update.message.reply_text("Я передам твой вопрос Татьяне.")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    print("✨ Девани запущена через Webhook")
    await app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url=WEBHOOK_URL
    )

if __name__ == '__main__':
    nest_asyncio.apply()
    asyncio.run(main())
