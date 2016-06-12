deluge-telegram-bot
=================
A bot that uses the Telegram API to notify a user when downloading is complete.

## Requirements
- A running installation of Deluge (+ enable 'Execute' plugin)
- Python 2.6+ (also required for Deluge, so should be okay)
- [Python Telegram Bot](https://pypi.python.org/pypi/python-telegram-bot) (handy to also have `pip` installed so you can easily install this package)

## Installation

> Note for step 1 and 4: I found that removable media (like an external hdd) cannot have executable files by default. I solved this by not having this script on the external device, but there are other mount options to fix this.

1. Clone repository to your computer
2. Create a Telegram API Token ([talk to BotFather](https://telegram.me/botfather))
3. Add token to `config.json` file
4. Make sure downloadcomplete.py is executable (`chmod u+x downloadcomplete.py`)
5. Do a test run by calling `python downloadcomplete.py idHere nameHere locHere`
6. Open Deluge Execute plug-in and add new command for torrent complete. Should look something like `~/scripts/deluge-telegram-bot/downloadcomplete.py`

## Wish list
- Add new torrents to deluge by providing a search (then giving a few results to choose from)
- Create additional feature for updating OSMC library from Telegram
