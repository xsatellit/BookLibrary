from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton

# Importing the Authors class from the GetAuthors module
from functions.default.GetAuthors import Authors

# Importing the Keyboard class from the CreateKeyboard module
from functions.default.CreateKeyboard import Keyboard

# This function will be triggered when the user sends the command '/aut'
@Client.on_message(filters.command('aut'))
async def handle_authors(app: Client, message: Message):
    # Create an instance of the Authors class
    authors_instance = Authors()
    
    # Get the first 50 authors from the database
    authors_list = authors_instance.getAuthorsList()[:50]
    
    # Close the connection to the database
    authors_instance.database.conn.close()

    # Send a message to the user with the list of authors and the keyboard
    await app.send_message(
        message.chat.id,
        "\n".join(authors_list),  # Join the authors into a single string separated by line breaks
        reply_markup=Keyboard().getKeyboartInSameLine(["Página Anterior", "Próxima Página"], ["Aut_0", "Aut_2"]) 
    )