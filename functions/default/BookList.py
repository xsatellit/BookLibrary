from helpers.jsonHandler import jsonHandler
from unidecode import unidecode


class BookList:
    """Class responsible for handling book lists."""

    def __init__(self) -> None:
        """Class constructor, which initializes the books attribute using a jsonHandler object."""
        self.books = jsonHandler()

    def __createListStr__(self, category: str) -> str:
        """Private method that creates a list of books as a string for a given category."""
        values = self.books.getAllValuesForSubKey(category, "Telegram")
        result = []

        for value in values:
            until = value.find("-")
            bookTelegram = value[0:until].strip()
            name = value[until:len(value)].strip()

            result.append(bookTelegram + " " + name + "\n")

        return '\n'.join(result)

    def getList(self, category: str) -> list:
        """Method that returns a list of books for a given category."""
        values = self.books.getAllValuesForSubKey(category, "Telegram")
        result = []

        for value in values:
            until = value.find("-")
            bookTelegram = value[0:until].strip()
            name = value[until:len(value)].strip()

            result.append(bookTelegram + " " + name + "\n")

        return result

    def getListStr(self, category: str) -> str:
        """Method that returns a string with the list of books for a given category."""
        if category == "Aventura":
            return self.__createListStr__("Aventura")
        elif category == "Biografia":
            return self.__createListStr__("Biografia")
        elif category == "Drama":
            return self.__createListStr__("Drama")
        elif category == "Fantasia":
            return self.__createListStr__("Fantasia")
        elif category == "FiccaoCientifica":
            return self.__createListStr__("FiccaoCientifica")
        elif category == "Romance":
            return self.__createListStr__("Romance")

    def searchBookName(self, bookName: str) -> str:
        """Method that returns the 'Name' attribute from a book, e.g. /BookName"""
        bookList = self.books.getAllkeys()
        bookName = unidecode(bookName)
        match = [book for book in bookList if bookName.lower()
                 in unidecode(book.lower())]

        return self.books.getValueForSubKey(match[0], "Name")

    def getBook(self, bookID: int) -> str:
        return self.books.getKeyForSubkey("ID", bookID)

    def updateBooks(self) -> None:
        """Method that updates the books attribute with a new jsonHandler object."""
        self.books = jsonHandler()
