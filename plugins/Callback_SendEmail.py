# Import necessary modules
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
import subprocess

# Import custom module to interact with the database
from database.Database import DatabaseFunctions


# Define a callback function to handle the 'Kindle' button press
@Client.on_callback_query(filters.regex(r"^(Kindle_)"))
async def sendEmail_handler(app: Client, callback: CallbackQuery):
    # Create a database connection
    database = DatabaseFunctions()

    # Extract the book ID from the callback data
    callb, book_id = callback.data.split("_", 2)

    # Get the email address of the user who pressed the button
    try:
        user_email = database.getUserEmail(callback.from_user.id)
    except:
        await app.send_message(
            callback.from_user.id,
            "Não foi possível encontrar seu email Kindle no sistema, por favor, verifique se está cadastrado utilizando o comando /email e clicando no botão Cadastrar email."
        )

    # Close the database connection
    database.conn.close()

    # Construct the command to run the 'SendEmail.py' script
    command = f"functions/default/SendEmail.py {user_email} {book_id}"
    command = command.replace("\n", "")

    # Execute the command to run the 'SendEmail.py' script as a subprocess
    subprocess.Popen(r'python %s' % (command), shell=True)


