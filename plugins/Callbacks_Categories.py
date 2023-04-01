# necessary modules
from pyrogram import Client, filters
import re
from pyrogram.types import CallbackQuery

# custom modules
from functions.default.CreateKeyboard import Keyboard
from functions.default.BookList import BookList
from functions.default.GeneratePage import generate_page


# Define a function for handling callback queries (e.g. when the user clicks a navigation button)
@Client.on_callback_query()
async def handle_categories(app: Client, callback: CallbackQuery):
    """This function returns a list of books grouped by category. If there are more than 50 books in a category, they are split into multiple 
    'pages', each containing up to 50 books. This is necessary because Telegram has a limit on the length of messages that can be sent. 
    By splitting the books into pages, we can ensure that each page's message length does not exceed Telegram's limit."""
    
    # instance of the BookList class
    books = BookList()

    # id of user
    user_id = callback.from_user.id

    # If the callback data contains an underscore, it means the user clicked a navigation button
    if "_" in callback.data:
        category, offset = callback.data.split("_", 1)
        offset = int(offset)
    # Otherwise, the user clicked a category button
    else:
        category = callback.data
        offset = 1
    
    # If there are more than 50 books in the category, split them into pages
    if len(books.books.getAllValuesForSubKey(category, "Telegram")) > 50:
        
        # Generate the current page's text and navigation buttons
        generator = generate_page(category, books.getList(category), offset)
        texto = generator[category]["texto"]
        reply_markup = Keyboard().getKeyboardFromDict([
            generator[category][f"{category}_{offset - 1}"],
            generator[category][f"{category}_{offset + 1}"]
        ])
        
        # Edit the previous message with the new page's text and navigation buttons, 
        # or just sends the message if the user clicked in a category button
        try:
            if "_" in callback.data:
                await callback.edit_message_text(texto, reply_markup=reply_markup)
            else:
                await app.send_message(user_id, f"🪙 Livros disponíveis na categoria {category}:")
                await app.send_message(user_id, texto, reply_markup=reply_markup)
        except:
            ...

    # If there are 50 or less books in the category, just sends the list
    else:
        await app.send_message(user_id, f"🪙 Livros disponíveis na categoria {category}:")
        await app.send_message(user_id, books.getListStr(callback.data))
