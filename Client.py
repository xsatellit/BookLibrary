from pyrogram import Client
from serverConfig.Config import SESSION_NAME, API_HASH, API_ID, BOT_TOKEN
from pyromod import listen

app = Client(
    name=SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    try:
        print("Bot iniciado")
        app.run()
    except Exception as e:
        print(f"Error occurred at Client.py --> {e}")
        pass