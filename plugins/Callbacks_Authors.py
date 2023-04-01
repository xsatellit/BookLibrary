from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

from functions.default.GeneratePage import generate_page
from functions.default.GetAuthors import Authors
from functions.default.CreateKeyboard import Keyboard


@Client.on_callback_query(filters.regex(r"^(Aut_)"))
async def callback_authors(app: Client, callback: CallbackQuery):
    # extract callback and offset from callback data
    callb, offset = callback.data.split("_", 2)
    offset = int(offset)

    # get the authors list
    authorsInstance = Authors()
    authorsList = authorsInstance.getAuthorsList()
    authorsInstance.database.conn.close()

    # generate the page with the authors list
    generator = generate_page(callb, authorsList, offset)
    text = generator[callb]["texto"]

    # create the keyboard for navigating through the list of authors
    keyboard = Keyboard().getKeyboardFromDict(
        [
            generator[callb][f"{callb}_{offset-1}"],
            generator[callb][f"{callb}_{offset+1}"]
        ]
    )

    # try to edit the message with the new text and keyboard
    try:
        await callback.edit_message_text(text, reply_markup=keyboard)
    except:
        ...
