from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

from database.Database import DatabaseFunctions
from functions.default.CreateKeyboard import Keyboard


@Client.on_callback_query(filters.regex(r"^(AlterarEmail)"))
async def modifyEmail_handler(app: Client, callback: CallbackQuery):
    database = DatabaseFunctions()
    user_id = callback.from_user.id

    try:
        currentEmail = database.getUserEmail(user_id)

        answer = await callback.message.chat.ask(
            f"Seu email atual é: {currentEmail}, você tem certeza que deseja alterá-lo?\n\n<strong>Digite S para sim / N para não:"
        )

        if answer.text.lower().strip() == "s":
            database.removeUser(user_id)
            keyboard = Keyboard().getKeyboard(["Continuar"], ["CadastrarEmail"])
            await app.send_message(
                user_id,
                text="Clique no botão abaixo:",
                reply_markup=keyboard
            )
        elif answer.text.lower().strip() == "n":
            await app.send_message(
                user_id,
                "Procedimento cancelado.")
    except:
        await app.send_message(
            user_id,
            "Você não tem um email cadastrado no sistema.")
    
    database.conn.close()