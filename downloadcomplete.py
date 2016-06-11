import json, telegram, sys

# Load config from JSON file config.json
config = json.loads(open("config.json").read())

# Sends message to Telegram bot
def downloadComplete(bot, downloadName):
    cid = bot.getUpdates()[-1].message.chat_id	
    bot.sendMessage(chat_id=cid, text="Hi! I just completed a download of \"" + downloadName + "\" for you :)")

# Initiate bot
bot = telegram.Bot(token=config["token"])

# All ready, send the message!
# sys.argv[1] contains Deluge Execute plug-in passing 'download id'
# sys.argv[2] contains Deluge Execute plug-in passing 'download name'
# sys.argv[3] contains Deluge Execute plug-in passing 'download location'
downloadComplete(bot, sys.argv[2])
