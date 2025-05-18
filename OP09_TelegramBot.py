# OP09_TelegramBot

import telebot
import datetime
import time
import threading
import random

import config as conf

list = ["Некоторые учченые считают, что _Вода_ на Земле может быть _старше_ самой Солнечной системы(!): "
        "\n от 30% до 50% воды в наших океанах возможно присутствовала в межзвездном пространстве еще до формирования "
        "Солнечной системы около 4,6 миллиарда лет назад.",

"Горячая вода замерзает быстрее холодной: Это явление известно как эффект Мпемба. "
"Под определенными условиями горячая вода может замерзать быстрее, чем холодная, "
"хотя ученые до сих пор полностью не разгадали механизм этого процесса.",

"Больше воды в атмосфере, чем во всех реках мира: Объем водяного пара в атмосфере Земли в любой момент "
"времени превышает объем воды во всех реках мира вместе взятых. Это подчеркивает важную роль атмосферы "
"в гидрологическом цикле, перераспределяя воду по планете."]

random_fact = random.choice(list)
# --------------  --------------  -----------------------
bot = telebot.TeleBot(conf.bot_key)  # ключ -  token to access bot

@bot.message_handler(commands=['help'])
def help_massage(message):
    bot.reply_to(message, "/start начало работы \n/help подсказка (этот текст)  \n/fact информация о воде")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Приветствую! В этом чат боте масса информации, \n он может напоминать пить водичку!')
    now = datetime.datetime.now().strftime("%H:%M")
    print("T_start=" + now)
    print("Start_args=" )
    print((message.chat.id,))

    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id, ))
    reminder_thread.start()
    help_massage(message)

@bot.message_handler(commands=['fact'])
def fact_message(message):
    print(f"fact: chat_id=  {message.chat.id} ")
    random_fact = random.choice(list)
    bot.reply_to(message, f'Интересно, что: \n {random_fact}')
def send_reminders(chat_id):
    print(f"reminder ")
    first_rem  = "09:00"
    rem2 = "11:00"
    rem3 = "13:00"
    rem4 = "15:05"
    rem5 = "17:07"
    end_rem = "19:00"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if (now == first_rem or now == rem2 or now == rem3
                or now == rem4 or now == rem5 or now == end_rem):
            bot.send_message(chat_id, "Напоминание: Оторвитесь от важных дел! \n Выпейте водичку (стаканчик-другой)")
            time.sleep(61)
            print(f"reminder: {chat_id} T=" +now)
        time.sleep(1)

bot.polling(none_stop=True)
