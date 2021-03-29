from telegram.ext import Updater, CommandHandler
import telegram
import requests
import re

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi!, use /help command for more information")

def help(update, context):
    mesg = " It is a bot that uses /gimmedoge command to give random cute dog images"
    update.message.reply_text(mesg)

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents[ "url" ]
    return url

def gimmedoge(update, context):
    bot = telegram.Bot(token = "your_token")
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id= chat_id, photo = url)

def main():
    updater = Updater("your_token",use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("gimmedoge",gimmedoge))
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

