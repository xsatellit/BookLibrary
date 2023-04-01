from database.Database import DatabaseFunctions
from functions.default.BookList import BookList
import re
from unidecode import unidecode


class Authors:

    def __init__(self) -> None:
        self.database = DatabaseFunctions()

    def __getAuthorsDatabase__(self) -> list:
        return self.database.getAllBooksAuthors()
    
    def __separateAuthors__(self) -> list:
        authors = self.__getAuthorsDatabase__()
        for author in self.__getAuthorsDatabase__():
            if "," in author:
                author1, author2 = author.split(", ", 2)
                authors.remove(author)
                authors.append(author1.strip())
                authors.append(author2.strip())

        return authors

    def __setAuthorsList__(self) -> list:
        authors = self.__separateAuthors__()

        authorsList = list(set(authors))
        authorsList.sort()

        result = []
        for author in authorsList:
            authorMod = re.sub(r"[.’'\s-]", "", author)
            result.append("/" + unidecode(authorMod) + " - " + author + "\n")
        
        return result
    
    def getAuthorsList(self) -> list:
        result = self.__setAuthorsList__()
        self.database.conn.close()
        return result
    
    def getBooksByAuthor(self, author: str) -> str:
        # Remove any '/' characters from the author name
        author = author.replace("/", "")
        
        # Get the list of authors from the database
        authorsList = self.__separateAuthors__()

        # Search for the author name in the authors list
        for author_name in authorsList:
            if re.sub(r"[.’'\s-]", "", author_name) == author:
                author = author_name

        # Get the list of books written by the author
        bookList = self.database.getAllBooksByAuthor(author)
        self.database.conn.close()
        
        # Create a list of book names
        book_names = []
        for book in bookList:
            book_names.append(BookList().searchBookName(book) + " - " + book + "\n")
        
        
        # Join the list of book names into a single string and return it
        return '\n'.join(book_names)

