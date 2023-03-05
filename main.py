import InvestingCapture
import constants as key
import telebot
import os
import ScreenCapture as SC

print("bot started...")

bot = telebot.TeleBot(key.API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "/help for help")


@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "/help for help \n/start for start"
						  "\n/sendmeyourscreenshot for a screenshot of my computer"
						  "\n/BTCnow Xem biểu đồ Bitcoin hiện tại"
						  "\n/ETHnow Xem biểu đồ Ethereum hiện tại"
						  "\n/VNInow Xem biểu đồ VNIndex hiện tại"
						  "\n/LTCnow Xem biểu đồ Litecoin hiện tại")

@bot.message_handler(commands=['BTCnow', 'ETHnow', 'VNInow', 'LTCnow'])
def chartCaptureScreen(message):
	photoName = ''
	inmessage = message.text
	inmessage = inmessage[1:]
	if(inmessage=='BTCnow'):
		photoName = 'BINANCE%3ABTCUSD'
	if(inmessage=='ETHnow'):
		photoName ='BINANCE:ETHUSD'
	if (inmessage == 'VNInow'):
		photoName = 'HOSE%3AVNINDEX'
	if (inmessage == 'LTCnow'):
		photoName = 'BINANCE%3ALTCUSD'

	imageName = str(message.chat.id)
	home_dir = os.system("node takescreenshot.js '" +photoName +"' '"+imageName+"'")
#	price = InvestingCapture.investCapture(imageName, photoName)
	bot.send_message(message.chat.id, "Giá "+ inmessage[:3]+" hiện tại là: ")

	photo1 = open("photo/'"+imageName+"'.png", 'rb')
	bot.send_photo(message.chat.id, photo1)
	print(photoName)

@bot.message_handler(commands=['sendmeyourscreenshot'])
def computerScreenShot(message):

	imageName = str(message.chat.id)

	SC.screenShot(imageName)

	photo1 = open("photo/"+ imageName +".png", 'rb')
	bot.send_photo(message.chat.id, photo1)
	print("Photo Sent")




@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Sorry, I can't understand you! /help")
	print(message)

bot.infinity_polling()

