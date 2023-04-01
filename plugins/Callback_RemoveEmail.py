from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

from database.Database import DatabaseFunctions


@Client.on_callback_query(filters.regex(r"^(ExcluirEmail)"))
async def removeEmail_handler(app: Client, callback: CallbackQuery):
    database = DatabaseFunctions()
    user_id = callback.from_user.id

    try:
        currentEmail = database.getUserEmail(user_id)

        answer = await callback.message.chat.ask(
            f"Seu email atual é: {currentEmail}, você tem certeza que deseja excluí-lo?\n\n<strong>Digite S para sim / N para não:"
        )

        if answer.text.lower().strip() == "s":
            database.removeUser(user_id)
            await app.send_message(
                user_id,
                text="Seu email foi excluído do sistema."
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
