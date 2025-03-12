# bot.py
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('punkt_tab')

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)

trainer.train  ([
    "Hi",
    "How can I help you"
])

trainer.train ([
    "What is your name",
    "My name is Chatbot"])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input(" > ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
        
