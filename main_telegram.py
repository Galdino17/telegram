import telebot
import Camisas


bot = telebot.TeleBot("852989604:AAGT3s4YiF2XfmolAvJgKJ2T3BneaaGbyaQ")

@bot.message_handler(commands=['start', 'help', 'pedido'])
def send_welcome(message):
	bot.reply_to(message, "Olá, o que você precisa??")

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
	bot.reply_to(message, message.text)

bot.polling()
