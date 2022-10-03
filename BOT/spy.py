from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.last_name}, {update.effective_user.username}'
               f', {update.effective_user.language_code}, {update.message.date}, {update.message.text}\n')
    file.close()
