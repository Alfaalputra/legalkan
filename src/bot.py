import telebot
from query import Query

bot = telebot.TeleBot("6366181552:AAHVwGvFbRPUArUqYqKugox5ptgj2GVufOQ", parse_mode="markdown")
@bot.message_handler(commands=['start', 'stop'])
def send_welcome(message):
	bot.reply_to(message, "Selamat datang di LegalKan. Bot ini berisi seputar informasi Legal yang berlaku di Indonesia.")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	query = message.text
	qry = Query()
	result = qry.query_data(query=query)
	
	bot.reply_to(message, result)
	
bot.infinity_polling()