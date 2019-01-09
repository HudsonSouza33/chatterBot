#-*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer #Aqui faz o treino do bot
from chatterbot import ChatBot #ChatBot em si
import os

bot = ChatBot('Testando')
#bot = ChatBot('Testando', read_only=True) Para não fazer novamente o treino

bot.set_trainer(ListTrainer)

for treinos in os.listdir('pasta'):
	chats = open('pasta/' + treinos, 'r').readlines()
	bot.train(chats)

while True:
	pergunta = input('Você: ')

	resposta = bot.get_response(pergunta)
	print('Bot: ' + str(resposta))