from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

from functions.admin.admin import Admin


@Client.on_callback_query(filters.regex(r"^(Cargo_)"))
async def handle_admin(app: Client, callback: CallbackQuery):
    user_id = callback.from_user.id
    database = Admin()
    
    if database.checkAdmin(user_id) == 1:
        if callback.data == "Cargo_Adicionar":
            user_id = await callback.message.chat.ask(
                "Digite o ID do usuário: "
            )

            user_id = int(user_id.text)

            user_type = await callback.message.chat.ask(
                "Digite o tipo de administrador: "
            )

            user_type = int(user_type.text)

            name = await callback.message.chat.ask(
                "Digite o nome do administrador: "
            )

            app.send_message(user_id, database.addAdmin(user_id, user_type, name))
                
        elif callback.data == "Cargo_Editar":
            user_id = await callback.message.chat.ask(
                "Digite o ID do usuário: "
            )

            user_id = int(user_id)

            user_type = await callback.message.chat.ask(
                "Digite o novo tipo de administrador: "
            )

            user_type = int(user_type.text)

            app.send_message(user_id, database.updateAdminType(user_id, user_type))

        elif callback.data == "Cargo_Remover":
            user_id = await callback.message.chat.ask(
                "Digite o ID do usuário: "
            )


            user_id = int(user_id)

            app.send_message(user_id, database.removeAdmin(user_id))
    
    # Closes connection to the database
    database.database.conn.close()