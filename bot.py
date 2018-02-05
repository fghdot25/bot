from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json


updater = Updater(token='526805602:AAFNxp2L5NEREowzj6Fjzxf5eg26o6Jmvfc')
dispatcher = updater.dispatcher


def startCommand(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Hello, let\'s talk? What is your name?')
	

def textMessage(bot, update):
	request = apiai.ApiAI('1fe47b27ff0748958f80b94c6c0cb0d4').text_request()
	
	#	bot.send_message(chat_id=update.message.chat_id, text = 'О, сәлем Жаңыл! Талғат сен туралы айтқан. Өткен туылған күніңмен, ақшаң көп болсын достарың сияқты!')
	request.lang = 'ru'
	request.session_id = 'paldotbot'
	request.query = update.message.text
	responseJson = json.loads(request.getresponse().read().decode('utf-8'))
	response = responseJson['result']['fulfillment']['speech']

	if response:
		bot.send_message(chat_id=update.message.chat_id, text=response)
    	#bot.send_message(chat_id=update.message.chat_id, text = 'О, сәлем Жаңыл! Талғат сен туралы айтқан. Өткен туылған күніңмен, ақшаң көп болсын достарың сияқты!')
	else:
		bot.send_message(chat_id=update.message.chat_id, text='I don\'t understand you!')



start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()
