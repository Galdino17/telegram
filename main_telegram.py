import telebot
import Camisas

def oi(message):
	message = str(message)
	if message.lower() == "oi" or message.lower() == "ola":
		return True
	else:
		return False

bot = telebot.TeleBot("852989604:AAGT3s4YiF2XfmolAvJgKJ2T3BneaaGbyaQ")

@bot.message_handler(commands=['start', 'help', 'pedido'])
def send_welcome(message):
	bot.reply_to(message, "Olá, o que você precisa?? Estou executando pelo Heroku.")

@bot.message_handler(commands=['Estoque'])
def send_welcome(message):
	try:
		mensagem  = str(Camisas.retornar_pedidos()[0])
		nome_do_usuario = str(message.chat.first_name)
		bot.reply_to(message, "Olá " + nome_do_usuario + ", \n \n Temos um total de " + mensagem + " livros no Estoque.")
	except Exception as e:
		print(mensagem[0])
		print(e)
		bot.reply_to(message, "Ops, tivemos um erro.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if oi(message.text):
		bot.reply_to(message, "Olá, o que você precisa?? Estou executando pelo Heroku.")
	else:
		bot.reply_to(message, "Ops, não reconhecemos esse comando: " + message.text[1:])

bot.polling()
