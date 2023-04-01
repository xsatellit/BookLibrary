from pyrogram import Client
from pyrogram import filters

from functions.asyncs import GetBookInfo
from functions.default.BookList import BookList

@Client.on_message(filters.command('pesquisar'))
async def search(app: Client, message: str) -> None:
    messageMod = message.text.replace('/pesquisar ', '')
    user_id = message.chat.id
    
    try:
        bookName = BookList().searchBookName(messageMod.strip())

        await GetBookInfo.createInformatioBox(app, user_id, bookName)
    
    except:
        await app.send_sticker(
            user_id, 
            "CAACAgIAAxkBAAIHN2QTlEYQQ3VMxGPGXrG_5YCBcF39AALrGQACn79JSIWnPS58gd44HgQ"
        )

        await app.send_message(
            user_id,
            f"Infelizmente não consegui encontrar o livro <strong>'{messageMod}'</strong> na biblioteca... Talvez você esqueceu alguma letra ou acento?\nOu... Ele ainda não chegou aqui..."
        )