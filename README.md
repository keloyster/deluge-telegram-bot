# deluge-telegram-bot
Caution: still in the works. Not ready yet.
A bot that uses the Telegram API to notify a user when downloading is complete.

# Requirements
- A running installation of Deluge (+ enable 'Execute' plugin)
- Python 2.6+
- Python Telegram Bot ( https://pypi.python.org/pypi/python-telegram-bot )

# Installation
- Clone repository to your computer
- Create a Telegram API Token
- Add token to config.json file
- Do a test run by calling 'python downloadcomplete.py idHere nameHere locHere'
- Add script to Deluge Execute Plugin

# Wish list
- Add new torrents to deluge by providing a search (then giving a few results to choose from)
- Create additional feature for updating OSMC library from Telegram
