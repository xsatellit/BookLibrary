from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from functions.default.CreateKeyboard import Keyboard


@Client.on_message(filters.command('email'))
async def email_handler(app: Client, message: Message) -> None:
    list_names_keyboard = ["Cadastrar email", "Alterar email cadastrado", "Excluir email cadastrado"]
    list_callb = ["CadastrarEmail", "AlterarEmail", "ExcluirEmail"]

    keyboard = Keyboard().getKeyboard(list_names_keyboard, list_callb)

    await app.send_message(
        message.chat.id,
        "<strong> SELECIONE UMA OPÇÃO: </strong>",
        reply_markup=keyboard
    )