from pyrogram.types import InlineKeyboardButton

# Define a function for generating book list pages
def generate_page(data: str, text: list, offset: int) -> dict:
    """The generate_page function takes in the callback data, a list of text, and an offset value as input. 
    It creates a dictionary containing the text to be sent as a message, along with the previous and 
    next page buttons represented as InlineKeyboardButton objects."""
    
    # Slice the list of text to only include the current page's worth of books
    text = text[:50] if offset == 1 else text[(offset-1)*50:min(offset*50, len(text))]
    
    # Create a dictionary containing the text and navigation buttons for the current page
    pages = {
        data: {
            f"{data}_{offset-1}": InlineKeyboardButton("Página Anterior", callback_data=f"{data}_{offset-1}"),
            f"{data}_{offset+1}": InlineKeyboardButton("Próxima Página", callback_data=f"{data}_{offset+1}"),
            "texto": '\n'.join(text)
        }
    }
    
    return pages