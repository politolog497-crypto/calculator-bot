import math
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧮 Научный калькулятор\n\nОтправь выражение!\n\nПримеры:\n2 + 2\nsqrt(16)\nsin(pi/2)\nasin(1)\nlog(100)\n2**10\nfactorial(5)"
    )

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    expr = update.message.text.strip()
    safe_dict = {
        "sin": math.sin, "cos": math.cos, "tan": math.tan,
        "asin": math.asin, "acos": math.acos, "atan": math.atan,
        "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
        "ln": math.log, "exp": math.exp,
        "factorial": math.factorial,
        "abs": abs, "ceil": math.ceil, "floor": math.floor,
        "pi": math.pi, "e": math.e,
    }
    try:
        result = eval(expr, {"__builtins__": {}}, safe_dict)
        if isinstance(result, float):
            result = round(result, 10)
        await update.message.reply_text(f"✅ {expr} = {result}")
    except ZeroDivisionError:
        await update.message.reply_text("❌ Деление на ноль!")
    except Exception:
        await update.message.reply_text("❌ Ошибка! Проверь выражение.\nНапиши /start для примеров.")

def main():
    TOKEN = "8545099129:AAEJXayxwjy5gix2c6LAJQsRG5MAegJg4P4"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))
    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
