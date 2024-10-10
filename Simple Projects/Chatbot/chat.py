from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Robo')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

trainer.train([
    'Hi',
    'Hello',
    'I need your assistance regarding my order',
    'Please elaborate, your concern',
    'How long it will take to receive an order ?',
    'I am fine!',
    'Okay Thanks',
    'No Problem! Have a Good Day!'
])

response1 = chatbot.get_response('Hello, how are you?')
response2 = chatbot.get_response('Unfortunately, I can not help you with this issue')


print(response1)
print(response2)