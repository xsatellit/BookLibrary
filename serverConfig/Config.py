from dotenv import load_dotenv
import os

# Server Configuration
load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'serverConfig', 'cred.env'))

SESSION_NAME = "Biblioteca Sáfica"
BOT_TOKEN = os.getenv("API_KEY")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")


# Lists of pattern configurations
LIST_OF_CATEGORIES = 'Aventura', 'Biografia', 'Drama', 'Fantasia', 'Ficção Científica', 'Romance'
LIST_OF_CALLBACKS_CATEGORIES = 'Aventura', 'Biografia', 'Drama', 'Fantasia', 'FiccaoCientifica', 'Romance'

LIST_OF_CALLBACKS_BOOKTYPES = ['PDF', 'EPUB', 'MOBI']

LIST_OF_SUPPORTED_FILES = ['.doc', '.docx', '.rtf', '.htm', '.html', '.txt', '.zip', '.mobi', '.epub', '.pdf', '.jpg', '.gif', '.bmp', '.png', 'pdf', 'doc',
                           'docx', 'rtf', 'htm', 'html', 'txt', 'zip', 'mobi', 'epub', 'jpg', 'gif', 'bmp', 'png']

# Email Configuration
HOST = ""
PORT = ""
LOGIN = ""
PASSWORD = ""
