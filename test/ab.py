from telegram.ext import Application, CommandHandler
import os

# Fetch the bot token from the environment variables
BOT_TOKEN = os.getenv('TOKEN')

# Define a function that handles the /start command
async def start(update, context):
    await update.message.reply_text('Hi!')

# Create the Application and pass your bot's token
application = Application.builder().token(BOT_TOKEN).build()

# Register the /start command handler
application.add_handler(CommandHandler('start', start))

# Start the bot
application.run_polling()
