import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("6232063256:AAHUI1xCSHw-QlQfwVE4m1xS-b7dOgP1h3U")

START_TEXT = """Привет! Я Амина — врач. Сама прошла через операцию, поэтому знаю этот путь не только как врач, но и как пациент.  Консультирую по двум направлениям:  — Подготовка к операции, — Реабилитация после операции. Напиши, что тебя интересует."""

PRICE_TEXT = """У меня три формата:  1. Мини-консультация — 2 500 ₽ - 30 минут, онлайн. Что сдать, как подготовиться, что взять с собой.  2. Полная консультация — 5 500 ₽ - 60 минут, онлайн или очно в Москве. Полный разбор ситуации. 3. Сопровождение — 17 000 ₽ - 3 встречи"""

PAY_TEXT = """Отлично, записываю тебя!  Для подтверждения — предоплата 50% на карту Сбербанк: [номер карты]  После оплаты напиши мне — и я пришлю дату и ссылку на звонок (или адрес, если очно).  Жду тебя"""

THINK_TEXT = """Cкажу вот что:  Когда я сама готовилась к операции, я потратила кучу времени на форумы, противоречивые статьи и советы подруг. За час со мной ты получаешь именно то, что я тогда хотела иметь рядом - врача. Но решать тебе — я не тороплю!"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_TEXT)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "прайс" in text:
        await update.message.reply_text(PRICE_TEXT)

    elif "оплат" in text:
        await update.message.reply_text(PAY_TEXT)

    elif "дорого" in text or "подумаю" in text:
        await update.message.reply_text(THINK_TEXT)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("Bot started")
app.run_polling()
