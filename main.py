import constants as key
import telebot
import Responses as R

print("bot started...")

bot = telebot.TeleBot(key.API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "/help for help")


@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "/help for help \n/start for start")


@bot.message_handler(commands=['yourphoto'])
def send_image(message):
	with open('C:/Users/PHAMHONGDANG/PycharmProjects/pythonProject/photo/tradingview.png', 'rb') as f:
		image_data = f.read()

	# Send the image to the chat where the /image command was typed
	bot.send_photo(chat_id=message.chat.id, photo=image_data)


@bot.message_handler(commands=['photo'])
def msg4(message):
	photo1 = open("C://Users//PHAMHONGDANG//Downloads//tradingview.png", 'rb')
	bot.send_photo(message.chat.id, photo1)
	print("Photo Sent")



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Sorry, I can't understand you! /help")
	print(message)

bot.infinity_polling()

