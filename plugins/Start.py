"""
This code defines a command handler for the /start command. 
When the command is received, the code chooses a random image URL from a list of 
pre-defined URLs, and sends that image along with a caption to the chat. 
The Messages().getText_start() method is used to retrieve the text for the caption from a separate file.
"""

from pyrogram import Client, filters
from random import choice
from defaultMessages.Messages import Messages
from functions.default.CreateKeyboard import Keyboard

# Define a command handler for the '/start' command.
@Client.on_message(filters.command('start'))
async def start(app: Client, message: str) -> None:
    # Define a list of image URLs to choose from.
    my_list = [
        'https://static1.srcdn.com/wordpress/wp-content/uploads/2020/07/Marceline-and-Bubblegum-Lesbian-Pride-Flag.jpg',
        'https://www.thefandomentals.com/wp-content/uploads/2016/12/bubbline-cover2.png',
        'https://static1-br.millenium.gg/articles/4/67/24/@/99995-e4gjxrvvoamgz07-article_cover_bd-1.jpg',
        'https://i.pinimg.com/originals/0e/3f/ed/0e3fed55a757ff80c5d7ea458cebe99f.jpg',
        'https://static1-br.millenium.gg/articles/3/74/53/@/104896-arte-do-conto-ascenda-comigo-foto-riot-gamesreproducao-article_m-1.png']
    # Choose a random image from the list.
    c = choice(my_list)
    # Send the image to the chat along with a caption.
    await app.send_photo(message.chat.id, c, caption=Messages().getText_start())


    

