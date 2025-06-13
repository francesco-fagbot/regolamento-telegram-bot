from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = "7961117862:AAEUfWZBw2F64vrmrKvYHz0CSDZYu_x1RNk"

async def send_regolamento(update: Update, name=""):
    if name:
        intro = f"👋 Benvenuto {name}!\n\n"
    else:
        intro = ""
    testo = (
        "📢 *ATTENZIONE – REGOLAMENTO DEL GRUPPO* 📢\n\n"
        "🔞 Questo gruppo è *VIETATO AI MINORI.*\n\n"
        "👑 È riservato a veri maschi Padroni che si divertono a umiliare ed esibire schiavi sottomessi.\n\n"
        "🚪 Chi entra in questo gruppo *dichiara di essere maggiorenne* e *accetta di essere esposto ed esibito.*\n\n"
        "❌ NON sono ammesse richieste di denaro.\n\n"
        "📍 *TUTTI i sottomessi* che si presentano sono *OBBLIGATI a dire la loro LOCALITÀ*,\n"
        "per favorire incontri con i Padroni VICINI.\n\n"
        "📌 Per i Padroni la località è *FACOLTATIVA ma gradita*, per farsi contattare e onorare dagli schiavi.\n\n"
        "Benvenuto nel gruppo."
    )
    await update.message.reply_text(intro + testo, parse_mode="Markdown")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await send_regolamento(update, user.first_name)

async def regolamento_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_regolamento(update)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    app.add_handler(CommandHandler("regolamento", regolamento_command))
    print("Bot attivo. In attesa di nuovi utenti o comandi manuali...")
    app.run_polling()
