import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
import requests 
import json

bot = telepot.Bot('telegram bot token')

def handle(msg):
    pprint(msg)
    chat_id = msg['chat']['id']
    from_id = msg['from']['id']
    #cat api
    DATA = "https://api.thecatapi.com/v1/images/search"
    req = requests.get(DATA)
    req_json = req.json()
    img_url = req_json[0]['url']
    photo = img_url
    
    bot.sendPhoto(chat_id, photo)

MessageLoop(bot, handle).run_as_thread()
print("I'm listening...")

while 1:
    time.sleep(5)