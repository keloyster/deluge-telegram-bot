#!/usr/bin/env python
import os, json, telegram, sys, logging

workingDir = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename=workingDir + '/bot.log', filemode='w', level=logging.DEBUG)
logging.info("Starting bot")

# Load config from JSON file config.json
config = json.loads(open(workingDir + "/config.json").read())

# Sends message to Telegram bot
# Parameters downloadId and downloadLocation given by Deluged but not used
def downloadComplete(bot, downloadId, downloadName, downloadLocation):
    cid = bot.getUpdates()[-1].message.chat_id	
    bot.sendMessage(chat_id=cid, text=config["message"].format(downloadName))

# Initiate bot
bot = telegram.Bot(token=config["token"])

# All ready, send the message!
# sys.argv[1] contains Deluge Execute plug-in passing 'download id'
# sys.argv[2] contains Deluge Execute plug-in passing 'download name'
# sys.argv[3] contains Deluge Execute plug-in passing 'download location'
downloadComplete(bot, sys.argv[1], sys.argv[2], sys.argv[3])
