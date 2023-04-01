from unidecode import unidecode
import os
import sys
sys.path.append('./database/')

from Database import DatabaseFunctions


class SearchFiles:
    
    """Class for searching files in the 'books' directory"""

    def searchFile(self, bookName: str, extension: str) -> str:
        """
        Searches for a file in the 'books' directory that matches the given book name and file extension.
        
        Returns:
        str: The absolute path of the first file found that matches the given criteria, or None if no file is found.
        """
        extension = f'.{extension}'.lower()
        bookName = unidecode(bookName)

        # Get the directory containing the file with the SearchFiles class
        class_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the books directory relative to the class file directory
        books_dir = os.path.join(class_dir, '../..', 'books', 'synopsis')
        matches = [os.path.join(root, file) for root, _, files in os.walk(books_dir)
                   for file in files if file.endswith(extension) and bookName.lower().strip() in unidecode(file.lower())]

        if matches:
            return matches[0]
        else:
            return None

    def searchFileByID(self, bookID: int, extension: str) -> str:
        """
        Searches for a file in the 'books' directory that matches the name of the book with the given ID and file extension.
        
        Returns:
        str: The absolute path of the first file found that matches the given criteria, or None if no file is found.
        """
        database = DatabaseFunctions()
        bookName = database.getBookName(bookID)
        database.conn.close()
        return self.searchFile(bookName, extension)
    
    def removeFile(self, fileName, extension) -> str:
        filepath = self.searchFile(fileName, extension)
        if os.path.exists(filepath):
            os.remove(filepath)
        else:
            raise RuntimeError("O arquivo não foi encontrado para remoção.")
