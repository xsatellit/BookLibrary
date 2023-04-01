from pyrogram import Client
from pyrogram import filters

# Importing the list of categories and callback data values
from serverConfig.Config import LIST_OF_CATEGORIES, LIST_OF_CALLBACKS_CATEGORIES

# Importing the CreateKeyboard function to generate the inline keyboard
from functions.default.CreateKeyboard import Keyboard


@Client.on_message(filters.command('cat'))
async def cat(app: Client, message: str) -> None:
    """The cat function is a command handler function that creates an inline keyboard containing 
    the list of available book categories. It sends the keyboard as a reply to the user who called 
    the command."""

    # Using the CreateKeyboard function to generate the inline keyboard
    categories = Keyboard().getKeyboard(
        LIST_OF_CATEGORIES, LIST_OF_CALLBACKS_CATEGORIES)

    # Sending the inline keyboard as a message to the user who called the command
    await app.send_message(
        message.chat.id,
        '<strong>           SELECIONE UMA OPÇÃO: </strong>',
        reply_markup=categories
    )
    