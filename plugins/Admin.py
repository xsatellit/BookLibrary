from pyrogram import Client, filters
from pyrogram.types import Message


# Importing the Keyboard class from the CreateKeyboard module
from functions.default.CreateKeyboard import Keyboard
from functions.admin.admin import Admin
from defaultMessages.Messages import Messages


# This function will be triggered when the user sends the command '/aut'
@Client.on_message(filters.command('adm'))
async def handle_adm(app: Client, message: Message):
    database = Admin()
    user_type = database.checkAdmin(message.chat.id)

    if user_type:
        role = database.getRole(user_type)
        name = message.chat.first_name
        picUrl = "https://tudosobrehospedagemdesites.com.br/site/wp-content/uploads/2016/10/painel-de-controle-hospedagem-topo-728x273.png"

        bookFuncCallb = ["Livro_Adicionar", "Livro_Editar", "Livro_Remover"]
        bookFuncNames = ["Adicionar Livro", 
                        "Editar Livro",
                        "Remover Livro"]

        usersFuncCallb = ["Cargo_Adicionar", "Cargo_Editar", "Cargo_Remover"]
        usersFuncNames = ["Adicionar Administrador",
                          "Editar Cargo",
                          "Remover Administrador"]
        
        if user_type == 1:
            bookFuncNames.extend(usersFuncNames)
            bookFuncCallb.extend(usersFuncCallb)
            keyboard = Keyboard().getKeyboard(bookFuncNames, bookFuncCallb)
        else:
            keyboard = Keyboard().getKeyboard(bookFuncNames, bookFuncCallb)

        await app.send_photo(
            message.chat.id,
            picUrl,
            caption=Messages().getText_AdmPanel(name, role),
            reply_markup=keyboard
        )
