from telegram import Update
from telegram.ext import ContextTypes

import model
import view


async def all_list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{view.view_user(model.show_users())}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/all\n/add Имя Фамилия телефон \n/find Фамилия \n/del №пользователя\n/help')


async def add_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    # print(msg)
    items = msg.split()  # /add Иванов Иван Иванович 123456789
    x = items[1]
    y = items[2]
    z = items[3]
    model.create_user([x, y, z])
    await update.message.reply_text(f'Пользователь {x}  {y}  {z} добавлен')


async def del_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()  # /del 1
    item = int(items[1]) - 1
    user = model.show_users()[item]
    deleted_user = f'№{int(items[1])}: {user[0]} {user[1]} {user[2]}'
    new_guide = model.delete_user(item, model.show_users())
    model.new_create_user(new_guide)  # Сохраняем новый справочник
    await update.message.reply_text(f'Пользователь {deleted_user} удален')


async def find_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    # print(msg)
    items = msg.split()  # /sum 123 1233
    surname = items[1]
    users = model.show_users()
    found_users = []
    for i in users:
        if i[1] == surname:
            found_users.append(i)
    # print(found_users)
    if found_users:
        st = view.view_user(found_users)
    else:
        st = 'Пользователи не найдены'

    await update.message.reply_text(f'{st}')
