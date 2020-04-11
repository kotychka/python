import telebot
# from telebot import apihelper

bot = telebot.TeleBot("1259408766:AAH7lYkYSyUwtSQU-g_VaQdDX2j4x0FaoYA")

# apihelper.proxy = {
#     'http': 'http://217.182.230.15:4469',
#     'https': 'http://217.182.230.15:4469',
# }

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hi, how are you doing?")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "There will be help")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_to(message, message.text)

# bot.polling()

def telegram_polling():
    try:
        bot.polling(none_stop=True, timeout=60) #constantly get messages from Telegram
    except:
        traceback_error_string=traceback.format_exc()
        with open("Error.Log", "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime("%c")+"\r\n<<ERROR polling>>\r\n"+ traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()
        time.sleep(10)
        telegram_polling()

if __name__ == '__main__':    
    telegram_polling()