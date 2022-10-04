from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

from pwd import TOKEN

bot_token = TOKEN

app = ApplicationBuilder().token(bot_token).build()
print('server start')
app.add_handler(CommandHandler("all", all_list_command))
app.add_handler(CommandHandler("del", del_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("add", add_command))
app.add_handler(CommandHandler("find", find_command))


app.run_polling()
