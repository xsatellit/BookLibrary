# Import necessary modules
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
import subprocess

# Import custom module to interact with the database
from database.Database import DatabaseFunctions
from functions.default.SearchFiles import SearchFiles


# Define a callback function to handle the 'Kindle' button press
@Client.on_callback_query(filters.regex(r"^(Kindle_)"))
async def sendEmail_handler(app: Client, callback: CallbackQuery):
    # Create a database connection
    database = DatabaseFunctions()

    # Extract the book ID from the callback data
    callb, book_id = callback.data.split("_", 2)

    # Get the email address of the user who pressed the button
    user_email = database.getUserEmail(callback.from_user.id)
    # Close the database connection
    database.conn.close()

    # Check if the user has an email
    if user_email is not None and SearchFiles().checkFile(book_id, "epub"):

        # Construct the command to run the 'SendEmail.py' script
        command = f"functions/default/SendEmail.py {user_email} {book_id}"
        command = command.replace("\n", "")

        # Execute the command to run the 'SendEmail.py' script as a subprocess
        subprocess.Popen(r'python %s' % (command), shell=True)

        await app.send_message(
            callback.from_user.id,
            "O livro foi enviado para seu email Kindle. Note que após o envio ser executado, o tempo de chegada em sua estante não dependerá do nosso servidor e sim do servidor do Kindle, por isto é recomendado aguardar alguns minutos antes de tentar reenviar o arquivo, pois não há como cancelar e você pode ter uma má experiência tendo que apagar várias cópias do mesmo livro."
        )
    # If the user doesn't have an email, then returns a message indicating the error
    else:
        await app.send_message(
            callback.from_user.id,
            "Não foi possível encontrar seu email Kindle no sistema ou o arquivo está indisponível. Para melhor diagnóstico, verifique se está cadastrado utilizando o comando /email e clicando no botão Cadastrar email."
        )




