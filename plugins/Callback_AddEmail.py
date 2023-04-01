from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

from database.Database import DatabaseFunctions
from defaultMessages.Messages import Messages


@Client.on_callback_query(filters.regex(r"^(CadastrarEmail)"))
async def handle_emailRegister(app, callback: CallbackQuery):
    database = DatabaseFunctions()
    person_name = callback.from_user.first_name

    if (database.checkUserExists(callback.from_user.id)):
        email = database.getUserEmail(callback.from_user.id)
        await app.send_message(
            callback.from_user.id,
            f"{person_name}, atualmente você já tem um email cadastrado no sistema: {email}\n\nCaso deseje alterá-lo, digite /email e siga as instruções."
        )
    
    else:
        
        await app.send_message(
            callback.from_user.id,
            Messages().getEmail_text(person_name),
            disable_web_page_preview=True)

        while True:
            answer = await callback.message.chat.ask(f"Digite seu email Kindle:")
            if "@kindle.com" in answer.text:
                confirm = await callback.message.chat.ask(f"Você tem certeza que deseja cadastrar o email {answer.text}? \n<strong>Digite S para Sim / N para não/ C para cancelar o cadastro.</strong>")
                if confirm.text.lower().strip() == "s":
                    database.addUser(callback.from_user.id, answer.text.strip())
                    await app.send_message(
                        callback.from_user.id,
                        "🤖 Seu email foi cadastrado, agora você pode enviar arquivos da biblioteca <strong>sem precisar registrá-lo novamente</strong> :)\n\nCaso ainda não tenha adicionado o e-mail da biblioteca na lista de e-mails aprovados, o endereço é: bibliotecabotlesb@gmail.com\n<strong>É necessário adicionar o email do bot na lista de emails aprovados ou não será possível receber os livros em seu kindle.</strong>\n\nCaso não saiba como aprovar um e-mail no seu kindle, <a href='https://www.amazon.com.br/gp/help/customer/display.html?nodeId=GX9XLEVV8G4DB28H'>clique aqui</a>.",
                        disable_web_page_preview=True
                    )
                    break

                elif confirm.text.lower().strip() == "n":
                    continue

                else:
                    await app.send_message(
                        callback.from_user.id,
                        "Cadastro cancelado.")
                    break

            else:
                await app.send_message(
                    callback.from_user.id,
                    "Leia as instruções e tente novamente.")
                break
    
    database.conn.close()
