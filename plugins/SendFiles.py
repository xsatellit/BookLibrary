from pyrogram import Client
from pyrogram.types import Message

from helpers.Filters import filters_used
from functions.asyncs import GetBookInfo
from functions.default.GetAuthors import Authors

@Client.on_message(filters_used)
async def send_Files(app: Client, message: Message):
    user_id = message.chat.id
    try:
        await GetBookInfo.createInformatioBox(app, user_id, message.text)
    except:
        try:
            authorsList = Authors().getBooksByAuthor(message.text)

            await app.send_message(
                user_id,
                authorsList
            )
        except:
            await app.send_sticker(
                user_id,
                "CAACAgIAAxkBAAIHQ2QTlPIUtc23uxmxr-dkytAe-7mUAALkFAACEEBRSJ9ELfiXdf_MHgQ"
            )
    


    
    
