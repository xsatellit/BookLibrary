from database.Database import DatabaseFunctions
from defaultMessages.Messages import Messages
from helpers.jsonHandler import jsonHandler
from functions.default.CreateKeyboard import Keyboard
from serverConfig.Config import LIST_OF_CALLBACKS_BOOKTYPES



async def createInformatioBox(app, user_id: int, message: str) -> None:
    """
    This function creates an information box for a given book, which includes its synopsis, author, and title, and 
    provides the user with a list of options to choose from. The available options are "Enviar para o Kindle" and 
    "Cadastrar email Kindle", as well as the different types of books.

    :param app: The Pyrogram client object.
    :type app: pyrogram.Client
    :param user_id: The user ID.
    :type user_id: int
    :param message: The message sent by user.
    :type message: str
    :return: None
    :rtype: None
    """
    database = DatabaseFunctions()

    book_id = jsonHandler().getAttr2ValueFromAttr1Value(message, "Name", "ID")
    synopsis = database.getBookSynopsis(book_id)
    author = database.getBookAuthor(book_id)
    bookName = database.getBookName(book_id)
    picUrl = database.getBookIMG(book_id)
    userType = database.getAdmType(user_id)

    database.conn.close()

    booktypes = [
        f'{booktype}_{book_id}' for booktype in LIST_OF_CALLBACKS_BOOKTYPES]
    keyboard_Inline = [
        ["Enviar para o Kindle", "Cadastrar email Kindle"],[f"Kindle_{book_id}", "CadastrarEmail"]
    ]

    keyboard_admin_names = ["Editar Livro", "Remover Livro"]
    keyboard_admin_callb = [f"Livro_Editar_{book_id}", f"Livro_Remover_{book_id}"]

    keyboard_admin = Keyboard().getKeyboartInSameLine(keyboard_admin_names, keyboard_admin_callb)

    keyboard = Keyboard().getKeyboardWithInSameLine(
        LIST_OF_CALLBACKS_BOOKTYPES,
        booktypes,
        keyboard_Inline[0],
        keyboard_Inline[1])

    await app.send_photo(
        user_id,
        picUrl
    )

    await app.send_message(
        user_id,
        Messages().getText_book(synopsis, author, bookName),
    )

    await app.send_message(
        user_id,
        '<strong>SELECIONE UMA OPÇÃO:</strong>',
        reply_markup=keyboard
    )

    if userType > 0:
        await app.send_message(
            user_id,
            '<strong>OPÇÕES DE ADMINISTRADOR:</strong>',
            reply_markup=keyboard_admin
        )