from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from defaultMessages.Messages import Messages
from functions.default.CreateKeyboard import Keyboard


@Client.on_message(filters.command('enviar'))
async def send_files(app: Client, message: Message) -> None:
    nome = message.chat.first_name
    user_id = message.chat.id

    if message.text == "/enviar":
        await app.send_message(
            user_id,
            Messages().getText_sendFiles(nome))

    if message.text == "/enviar meu arquivo":
        # Since the getButtons class needs a list as parameter and here is only needed a single element, we send the strings inside a []
        button = Keyboard().getKeyboard(
            ["Cadastrar emaill Kindle"], ["Cadastrar"])

        await app.send_message(
            user_id,
            "Para utilizar os serviços de envio, você precisa registrar seu endereço de email kindle no sistema. <strong>Caso ainda não tenha registrado, clique no botão abaixo para começar o cadastro</strong>. Senão, ignore esta mensagem.",
            reply_markup=button)

        await app.send_message(
            user_id,
            "<strong>Serviço indisponível no momento.</strong>"
        )


