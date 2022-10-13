import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler
from game28 import first_move, next_move_clever
from pwd import TOKEN

reply_keyboard = [['/play', '/help'], ['/exit']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

reply_keyboard2 = [['/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9', '/10'],
                   ['/11', '/12', '/13', '/14', '/15', '/16', '/17', '/18', '/19', '/20'],
                   ['/21', '/22', '/23', '/24', '/25', '/26', '/27', '/28', '/exit']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    global st
    st = 50
    update.message.reply_text(
        "Привет, поиграем в конфеты? play - начать игру, help - правила игры, exit - выход",
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        "Убираю клавиатуру. Наберите /start, чтобы она появилась опять",
        reply_markup=ReplyKeyboardRemove()
    )


def help(update, context):
    update.message.reply_text(
        'На столе лежит 50 конфет. Играют два игрока делая ход друг после друга.'
        ' Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.'
        ' Все конфеты оппонента достаются сделавшему последний ход.')


def play(update, context):
    global player1
    global player2
    global current_player
    player1 = update.message.from_user.first_name
    current_player = first_move(player1, player2)
    update.message.reply_text(f'Игра против бота, первым ходит {current_player}',
                              reply_markup=markup2)
    if current_player == player2:
        move_bot(update, context)


def move_bot(update, context):
    global st
    global current_player
    choice = next_move_clever(st)
    st -= choice
    update.message.reply_text(f'Выбор БОТа: {choice}, конфет осталось: {st} \n ')
    if st <= 0:
        update.message.reply_text(f'Победил: "БОТ"')
    else:
        current_player = player1
        update.message.reply_text(f'Сделайте ваш ход: {current_player} ')


def move_human(update, context):
    global st
    global current_player
    choice = int(update.message.text[1:])
    st -= choice
    update.message.reply_text(f'Выбор игрока {player1}: {choice}, конфет осталось: {st} ')
    if st <= 0:
        update.message.reply_text(f'Поздравляем, победил: "{player1}"')
    else:
        current_player = player2
        move_bot(update, context)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    for i in range(1, 29):
        dp.add_handler(CommandHandler(str(i), move_human))
    dp.add_handler(CommandHandler("play", play))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("exit", close_keyboard))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    current_player = ''
    player1 = 'Человек'
    player2 = 'Бот'
    st = 0
    main()
