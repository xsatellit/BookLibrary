from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

from functions.admin.admin import Admin
from functions.default.CreateKeyboard import Keyboard
from defaultMessages.Messages import Messages
from functions.default.SearchFiles import SearchFiles
from serverConfig.Config import LIST_OF_CATEGORIES


@Client.on_callback_query(filters.regex(r"^(Livro_)"))
async def handle_adminBook(app: Client, callback: CallbackQuery):
    user_id = callback.from_user.id
    database = Admin()

    if database.checkAdmin(user_id) > 0:

    # ----------------------------------------- >>   ADD BOOK   << ----------------------------------------------
        if callback.data == "Livro_Adicionar":
            await app.send_message(
                user_id,
                Messages.getText_AddBook()
            )
            await app.send_message(
                user_id,
                "Tendo certeza de que os pormenores acima estão esclacidos, vamos adiante."
            )
            book_category = await callback.message.chat.ask(
                "Digite a categoria do livro: (Aventura, Biografia, Drama, Fantasia, Ficcção Científica, Romance): "
            )

            # Will add the book but respecting the option to cancel, which will be handled by the exception (doing nothing)
            try:
                if book_category.text.lower() != "cancelar":
                    while book_category.text not in LIST_OF_CATEGORIES:
                        print(book_category.text)
                        book_category = await callback.message.chat.ask(
                            "Digite a categoria do livro: (Aventura, Biografia, Drama, Fantasia, Ficcção Científica, Romance): "
                        )
                    else:
                        book_title = await callback.message.chat.ask(
                            "Digite o título do livro:"
                        )
                    if book_title.text.lower() != "cancelar":
                        book_author = await callback.message.chat.ask(
                            "Agora, o autor/autores do livro. Caso haja mais que um, <strong>separe-os com uma vírgula</strong>. Exemplo: Joana Sobrenome, Maria Sobrenome."
                        )
                    if book_author.text.lower() != "cancelar":
                        book_command = await callback.message.chat.ask(
                            "Digite como será o comando utilizado para encontrar o livro. Ex: /NomeDoLivro"
                        )
                    if book_command.text.lower() != "cancelar":
                        book_synopsis = await callback.message.chat.ask(
                            "Agora, a sinopse do livro:"
                        )
                    if book_synopsis.text.lower() != "cancelar":
                        book_imageURL = await callback.message.chat.ask(
                            "Digite a url da imagem que será exibida como capa do livro na biblioteca:"
                        )
                    if book_imageURL.text.lower() != "cancelar":
                        await app.send_message(
                            user_id,
                            "⏳ Gerando amostra do livro..."
                        )

                        complete_message = Messages().getText_book(
                            book_synopsis.text, book_author.text, book_title.text)

                        await app.send_photo(
                            user_id,
                            book_imageURL.text
                        )
                        await app.send_message(
                            user_id,
                            complete_message
                        )
                        await app.send_message(
                            user_id,
                            f"{book_command.text} - {book_title.text} - {book_author.text}"
                        )

                        final_answer = await callback.message.chat.ask(
                            "Cheque as informações com cuidado. Caso estejam de acordo, digite <strong>continuar</strong>, ou, se houver alguma inconsistência, digite <strong>cancelar</strong>."
                        )

                        if final_answer.text.lower() == "continuar":
                            book_title = book_title.text.strip()
                            book_author = book_author.text.strip()
                            book_synopsis = book_synopsis.text.strip()
                            book_command = book_command.text.strip()
                            book_category = book_category.text.strip()
                            book_imageURL = book_imageURL.text.strip()
                            
                
                            # Try to add the book to the database
                            try:
                                database.addBook(book_title, book_author, book_synopsis)
                            except RuntimeError as e:
                                await app.send_message(
                                    user_id,
                                    e
                                )
                                return

                            book_id = int(database.getBookID(book_title))
                            
                            # Try to add the book image url to the database
                            try:
                                database.addBookIMG(book_id, book_imageURL)
                            except RuntimeError as e:
                                await app.send_message(
                                    user_id,
                                    e
                                )
                                return
                            
                            # Try to add the book to the json file
                            try:
                                database.addBookJson(book_title, book_author,
                                                book_id, book_command, book_category)
                            except RuntimeError as e:
                                await app.send_message(
                                    user_id,
                                    e
                                )
                                return
                            except ValueError as e:
                                await app.send_message(
                                    user_id,
                                    e
                                )
                                return
                            except TypeError as e:
                                await app.send_message(
                                    user_id,
                                    e
                                )
                                return
                            

                            await app.send_message(
                                user_id,
                                "O livro foi adicionado ao banco de dados."
                            )
                            keyboard = Keyboard().getKeyboard(["Adicionar arquivo PDF", "Adicionar arquivo EPUB", "Adicionar arquivo MOBI", "Concluir"],["Livro_AdicionarPDF", "Livro_AdicionarEPUB", "Livro_AdicionarMOBI", "Livro_Concluir"])

                            await app.send_message(
                                user_id,
                                "Agora, precisamos incluir os arquivos do livro no repositório. Quando estiver pronto, selecione uma opção para enviar.\n\n<strong> Não envie mais do que um arquivo por tipo </strong>, verifique seus arquivos antes de enviá-los e o faça apenas uma vez. Quando os três tipos forem recebidos, clique no botão 'Concluir'. \n\n<strong>Siga o modelo de título indicado pelas instruções.</strong>",
                                reply_markup=keyboard
                            )

            except:
                None
                

        elif callback.data == "Livro_AdicionarPDF":
            document = await callback.message.chat.ask(
                "Envie o arquivo PDF:"
            )
            document_type = document.document.file_name[-3:len(document.document.file_name)]

            if document_type != "pdf":
                await app.send_message(user_id, "Documento não é do tipo PDF. Tente novamente.")
            else:
                try:
                    await app.send_message(user_id, "Aguarde enquanto o download é concluído...")
                    await app.download_media(document, file_name=f'books/{document.document.file_name}')
                    await app.send_message(user_id, "Documento recebido com sucesso.")
                except Exception as e:
                    await app.send_message(user_id, f"O download do documento para o servidor não foi concluído. Erro:\n{e}")


        elif callback.data == "Livro_AdicionarEPUB":
            document = await callback.message.chat.ask(
                "Envie o arquivo EPUB:"
            )
            document_type = document.document.file_name[-4:len(document.document.file_name)]

            if document_type != "epub":
                await app.send_message(user_id, "Documento não é do tipo EPUB. Tente novamente.")
            else:
                try:
                    await app.send_message(user_id, "Aguarde enquanto o download é concluído...")
                    await app.download_media(document, file_name=f'books/{document.document.file_name}')
                    await app.send_message(user_id, "Documento recebido com sucesso.")
                except Exception as e:
                    await app.send_message(user_id, f"O download do documento para o servidor não foi concluído. Erro:\n{e}")

        elif callback.data == "Livro_AdicionarMOBI":
            document = await callback.message.chat.ask(
                "Envie o arquivo MOBI:"
            )
            document_type = document.document.file_name[-4:len(document.document.file_name)]

            if document_type != "mobi":
                await app.send_message(user_id, "Documento não é do tipo MOBI. Tente novamente.")
            else:
                try:
                    await app.send_message(user_id, "Aguarde enquanto o download é concluído...")
                    await app.download_media(document, file_name=f'books/{document.document.file_name}')
                    await app.send_message(user_id, "Documento recebido com sucesso.")
                except Exception as e:
                    await app.send_message(user_id, f"O download do documento para o servidor não foi concluído. Erro:\n{e}")

    # ----------------------------------------- >>   EDIT BOOK   << ----------------------------------------------

        elif callback.data == "Livro_Editar":
            await app.send_message(
                user_id,
                "Digite o comando do livro para encontrar o livro que deseja editar na biblioteca: "
            )

        elif "Livro_Editar_" in callback.data :
            callb, callb2, book_id = callback.data.split("_", 3)
            book_id = int(book_id)

            answer = await callback.message.chat.ask(
                "Digite uma opção para editar (digite apenas o número da opção. Ex: 1)):\n1.Nome\n2.Autor(a)\n3.Sinopse\n4.Capa\n5.Comando\n6.Arquivo PDF/EPUB/MOBI\n7.Cancelar"
            )

            if answer.text.strip() == "1":
                book_name = await callback.message.chat.ask(
                    "Digite o novo nome do livro: "
                )
                await app.send_message(
                    user_id,
                    database.updateBookName(book_id, book_name.text)
                )
            elif answer.text.strip() == "2":
                book_author = await callback.message.chat.ask(
                    "Digite o novo autor do livro: "
                )
                await app.send_message(
                    user_id,
                    database.updateBookAuthor(book_id, book_author.text)
                )
            elif answer.text.strip() == "3":
                book_synopsis = await callback.message.chat.ask(
                    "Digite a nova sinopse do livro: "
                )
                await app.send_message(
                    user_id,
                    database.updateBookSynopsis(book_id, book_synopsis.text)
                )
            elif answer.text.strip() == "4":
                book_url = await callback.message.chat.ask(
                    "Digite o link da nova capa do livro: "
                )
                await app.send_message(
                    user_id,
                    database.updateBookIMG(book_id, book_url.text)
                )
            elif answer.text.strip() == "5":
                newValue = await callback.message.chat.ask(
                    "Digite o novo comando do livro: "
                )
                await app.send_message(
                    user_id,
                    database.updateBookJson(book_id, newValue.text)
                )
            elif answer.text.strip() == "6":
                try:
                    book_name = database.database.getBookName(book_id)

                    book_extension = await callback.message.chat.ask(
                        "Digite a extensão que deseja remover: (PDF, EPUB ou MOBI)\nNão utilize pontos, apenas letras!"
                    )

                    SearchFiles().removeFile(book_name, book_extension.text.lower().strip())

                    keyboard = Keyboard().getKeyboard(["Adicionar arquivo PDF", "Adicionar arquivo EPUB", "Adicionar arquivo MOBI"],["Livro_AdicionarPDF", "Livro_AdicionarEPUB", "Livro_AdicionarMOBI"])
                    await app.send_message(
                        user_id,
                        "Agora, clique no botão correspondente abaixo para continuar: "
                    )
                except RuntimeError as e:
                    await app.send_message(
                        user_id,
                        f"Não foi possível concluir o procedimento. Erro: {e}"
                    )
        

    # ----------------------------------------- >>   REMOVE BOOK   << ----------------------------------------------

        elif callback.data == "Livro_Remover":
            await app.send_message(
                user_id,
                "Digite o comando do livro para encontrar o livro que deseja remover na biblioteca: "
            )
        elif "Livro_Remover_" in callback.data:
            callb, callb2, book_id = callback.data.split("_", 3)
            book_id = int(book_id)
            answer = await callback.message.chat.ask(
                "Você tem certeza que deseja remover este livro? A operação não poderá ser desfeita!\n\n<strong>S para sim / N para não </strong>"
            )

            if answer.text.lower().strip() == 's':
                try:
                    await app.send_message(user_id, "Removendo livro da biblioteca...")
                    await app.send_message(user_id, database.removeBook(book_id))
                except ValueError as e:
                    await app.send_message(user_id, e)
            else:
                await app.send_message(
                    callback.from_user.id,
                    "Operação cancelada."
                )


    # ----------------------------------------- >>   FINISH PROCEDURE   << ----------------------------------------------
        elif callback.data == "Livro_Concluir":
            await app.send_message(
                user_id,
                "Procedimento encerrado."
            )

    else:
        await app.send_message(
            user_id,
            "Você não pode realizar esta operação."
        )

    # Closes the connection to the database
    database.database.conn.close()
