# codice di giacomo turati
 
import schedule
import telebot
from threading import Thread
from time import sleep
import random
 
#token del bot
TOKEN = 'TOKEN'
 
#lista di fatti
fact = [
    "🌿ecco un fatto interessante sul basilico:\nIl basilico è originario dell'India e delle regioni tropicali dell'Asia. 🌍",
    "🌿ecco un fatto interessante sul basilico:\nIl suo nome scientifico è Ocimum basilicum. 🌿",
    "🌿ecco un fatto interessante sul basilico:\nIl basilico è una pianta aromatica appartenente alla famiglia delle Lamiaceae. 🌱",
    "🌿ecco un fatto interessante sul basilico:\nÈ ampiamente utilizzato nella cucina mediterranea per il suo sapore unico e aromatico. 👨‍🍳",
    "🌿ecco un fatto interessante sul basilico:\nEsistono diverse varietà di basilico, tra cui il basilico dolce, il basilico genovese e il basilico al limone. 🌿🍋",
    "🌿ecco un fatto interessante sul basilico:\nIl basilico è ricco di antiossidanti e contiene vitamine come la vitamina K, la vitamina A e la vitamina C. 💪🥦",
    "🌿ecco un fatto interessante sul basilico:\nSi crede che il basilico abbia proprietà medicinali, tra cui la capacità di ridurre l'infiammazione e migliorare la digestione. 🌿💊",
    "🌿ecco un fatto interessante sul basilico:\nIn molte culture, il basilico è considerato un simbolo di amore, prosperità e buona fortuna. 💕🍀"
]
 
#battute sul basilico
battute_sul_basilico = [
    "🌿 Ecco una battuta sul basilico: Perché il basilico è sempre allegro? Perché ha sempre le foglie in su! 😄",
    "🌿 Ecco una battuta sul basilico: Qual è il piatto preferito del basilico? La pesto-lagna! 🍝",
    "🌿 Ecco una battuta sul basilico: Cosa fa un basilico quando incontra un pomodoro? Lo sfoglia! 🍅",
    "🌿 Ecco una battuta sul basilico: Perché il basilico non gioca a carte? Perché odia le pietanze truffate! 🃏",
    "🌿 Ecco una battuta sul basilico: Come fa il basilico a chiamare un taxi? Prende il pesto! 🚖",
    "🌿 Ecco una battuta sul basilico: Qual è il supereroe preferito del basilico? Batman-basil! 🦸‍♂️",
    "🌿 Ecco una battuta sul basilico: Cosa dice un basilico in biblioteca? Silenzio, siamo in prestito! 📚",
    "🌿 Ecco una battuta sul basilico: Cosa dice un basilico quando cade? Pesto! 😱",
    "🌿 Ecco una battuta sul basilico: Cosa fa un basilico se si sente solo? Cerca un po' di pesto-compagnia! 🤝",
    "🌿 Ecco una battuta sul basilico: Perché il basilico non fa carriera? Perché preferisce stare tra le foglie! 🌱"
]
 
#diciamo che il bot si riferisce al token da noi inserito
bot = telebot.TeleBot(TOKEN, parse_mode=None)
 
def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)
 
id_chat = "ID CHAT" 
 
def get_chat_id(message):
    chat_id = message.chat.id
    # Salva l'ID della chat in una variabile
    my_variable = chat_id
 
def morning():
    return bot.send_message(id_chat, "Reminder giornaliero🕔\nMetti la pianta al sole!☀")
def night():
    return bot.send_message(id_chat, "Reminder giornaliero🕔\nRiporta la pianta in casa!🌛")
 
@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "🌿LISTA COMANDI:🌿\nstart - inizializza il bot🤖\nbattua - fa una battuta (poco) divertente🥗\nrandom_fact - informazioni interessanti sulla botanica🌱")
 
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Ciao! Sono Plant-AI 🎋, la piantina del futuro! Sarò qui per aiutarti a prenderti cura di me passo dopo passo 🌱.")
 
@bot.message_handler(commands=['random_fact'])
def send_fact(message):
	bot.reply_to(message, random.choice(fact))
 
@bot.message_handler(commands=['battuta'])
def send_pianta(message):
	bot.reply_to(message, random.choice(battute_sul_basilico))
 
if __name__ == "__main__":
    # Create the job in schedule.
    schedule.every().day.at("08:00", "Europe/Amsterdam").do(morning)
    schedule.every().day.at("20:00", "Europe/Amsterdam").do(night)
 
    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    Thread(target=schedule_checker).start() 
 
bot.polling() # type: ignore
