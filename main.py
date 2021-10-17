import telebot
import time

 TOKEN = "2080098767:AAEV-r97uNdN-lTya-t4AcxYH28Q-9W5yUM"
 bot = telebot.Telebot(TOKEN)

def getargs(text):
  _args = text.split()[1:]
  return _args


@bot.massage_handler(commands=["start"])
def sayhello(massage):
  bot.send_massage(massage.chat.id, "hellow I am Randikas Bot"
