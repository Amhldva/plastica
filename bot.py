from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "6232063256:AAHUI1xCSHw-QlQfwVE4m1xS-b7dOgP1h3U"

START_TEXT = """Привет! Я Амина — врач-хирург, сейчас специализируюсь на пластической хирургии.

Сама прошла через операцию, поэтому знаю этот путь не только как врач, но и как пациент.

Консультирую по двум направлениям:

— Подготовка к операции
(что сдать, как подготовить тело и голову, какие вопросы задать хирургу)

— Реабилитация после операции
(что нормально, что нет, как ускорить восстановление)

Форматы:
• Мини-консультация 30 мин — 2 500 ₽
• Полная консультация 60 мин — 5 500 ₽
• Пакет сопровождения (3 встречи) — 17 000 ₽

Онлайн или очно в Москве.

Напиши, что тебя интересует — и я отвечу на все вопросы."""

PRICE_TEXT = """Смотри, у меня три формата:

1. Мини-консультация — 2 500 ₽
30 минут, онлайн
Один конкретный вопрос: что сдать, как подготовиться, что взять с собой

2. Полная консультация — 5 500 ₽
60 минут, онлайн или очно в Москве
Полный разбор твоей ситуации + план действий

3. Сопровождение — 17 000 ₽
3 встречи: до операции, за день до и через месяц после
Я рядом на всём пути

Расскажи немного — что планируешь делать и на каком этапе сейчас? Подберу подходящий формат."""

PAY_TEXT = """Отлично, записываю тебя!

Для подтверждения — предоплата 50% на карту Сбербанк:
[номер карты]

После оплаты напиши мне — и я пришлю дату и ссылку на звонок (или адрес, если очно).

Жду тебя."""

THINK_TEXT = """Я могу объяснить, что входит — но честнее скажу вот что:

Когда я сама готовилась к операции, я потратила кучу времени на форумы, противоречивые статьи и советы подруг. И всё равно пришла неподготовленной.

За час со мной ты получаешь именно то, что я тогда хотела иметь рядом — врача, который прошёл через это сам и говорит без воды.

Но решать тебе — я не тороплю."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_TEXT)

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PRICE_TEXT)

async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PAY_TEXT)

async def think(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(THINK_TEXT)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("pay", pay))
app.add_handler(CommandHandler("think", think))

print("Бот запущен")
app.run_polling()