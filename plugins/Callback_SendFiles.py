from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from functions.default.SearchFiles import SearchFiles
from functions.default.BookList import BookList

# Define a callback function to handle when the user selects a file type (PDF, MOBI, or EPUB)
@Client.on_callback_query(filters.regex(r"^(PDF_|MOBI_|EPUB_)"))
async def handle_types(app: Client, callback: CallbackQuery):
    # Get the extension (PDF, MOBI, or EPUB) and the book ID from the callback data
    extension, bookID = callback.data.split("_", 1)

    user_id = callback.from_user.id
    
    # Get the name of the book corresponding to the given ID
    bookName = BookList().getBook(int(bookID))
    
    try:
        # Search for the path of the TXT file for the given book ID
        documentPath = SearchFiles().searchFileByID(bookID, extension)

        # Open the TXT file in binary mode using a 'with' statement, which automatically handles closing the file when we're done

        with open(documentPath, "rb") as document:
            # Send a message to the user to let them know the document is being sent
            await app.send_message(
                user_id, 
                "☁️  Estou enviando o arquivo para você, por favor, aguarde...")
            
            # Send the document to the user
            await app.send_document(
                user_id,
                document,
                file_name=f'{bookName}.{extension.lower()}'
            )
            
    except:
        await app.send_message(user_id, "Arquivo não encontrado no repositório de livros.")
