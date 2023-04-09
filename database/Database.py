import sqlite3


class DatabaseFunctions:
    """Class to intermediate and manage access to the database"""
    
    def __init__(self) -> None:
        try:
            self.conn = sqlite3.connect("libraryDB.db") # Create a connection to the database
        except sqlite3.IntegrityError as e:
            raise RuntimeError(f"IntegrityError occurred while connecting to server.\nError: {e}")
        except sqlite3.OperationalError as e:
            raise RuntimeError(f"IntegrityError occurred while connecting to server.\nError: {e}")
        
    def getAllBooks(self) -> dict:
        """
        Retrieve all books in the database and return a dictionary where
        the keys are book IDs and the values are tuples with the book name
        and author name.
        """

        cursor = self.conn.execute("SELECT * FROM books")
        row = {row[0]: (row[1], row[2]) for row in cursor.fetchall()}
        if row:
            return row
        else:
            raise RuntimeError(f"Database.py: Couldn't find any books in the database.")

    
    def getAllBooksID(self) -> list:
        """
        Retrieve a list of all book IDs in the database.
        """
        cursor = self.conn.execute("SELECT id FROM books")
        row = [row[0] for row in cursor.fetchall()]
        if row:
            return row
        else:
            raise RuntimeError(f"Database.py: Couldn't find any book id in the database.")

    def getAllBooksName(self) -> list:
        """
        Retrieve a list of all book names in the database.
        """
        cursor = self.conn.execute("SELECT name FROM books")
        row =  [row[0] for row in cursor.fetchall()]
        if row:
            return row
        else:
            raise RuntimeError(f"Database.py: Couldn't find any book in the database.")
    
    def getAllBooksAuthors(self) -> list:
        """
        Retrieve a list of all author names in the database.
        """
        cursor = self.conn.execute("SELECT author FROM books")
        row = [row[0] for row in cursor.fetchall()]
        if row:
            return row
        else:
            raise RuntimeError(f"Database.py: Couldn't find any author in the database.")

    def getAllUsersID(self) -> list:
        """
        Retrieve a list of all users IDs.
        """
        cursor = self.conn.execute("SELECT id FROM users")
        row = [row[0] for row in cursor.fetchall()]
        if row:
            return row
        else:
            raise RuntimeError(f"Database.py: Couldn't find any user id in the database.")

    # adm function
    def getAllAdm(self) -> dict:
        """
        Retrieve a dict of all adm IDs, types and names
        """
        cursor = self.conn.execute("SELECT * FROM adm")
        row = {row[0]: (row[1], row[2]) for row in cursor.fetchall()}
        if row:
            return row
        else:
            raise RuntimeError(f"Database.py: Couldn't find any adm in the database.")

    def getAllBooksByAuthor(self, author: str) -> list:
        """
        Retrieve a list of all book names for a given author name.
        """
        cursor = self.conn.execute("SELECT name FROM books WHERE author LIKE ?", ('%' + author + '%',))
        return [row[0] for row in cursor.fetchall()]
    
    def getBookID(self, bookName: str) -> int:
        """
        Retrieve the book ID for a given book name.
        """
        cursor = self.conn.execute("SELECT id FROM books WHERE name=?", (bookName,))
        row = cursor.fetchone()
        if row is not None:
            return int(row[0])

    def getBookName(self, bookID: int) -> str:
        """
        Retrieve the book name for a given book ID.
        """
        cursor = self.conn.execute("SELECT name FROM books WHERE id=?", (bookID,))
        row = cursor.fetchone()
        if row is not None:
            return str(row[0])

    def getBookAuthor(self, bookID: int) -> str:
        """
        Retrieve the author name for a given book ID.
        """
        cursor = self.conn.execute("SELECT author FROM books WHERE id=?", (bookID,))
        row = cursor.fetchone()
        if row is not None:
            return str(row[0])

    def getBookSynopsis(self, bookID: int) -> str:
        """
        Retrieve the synopsis for a given book ID.
        """
        cursor = self.conn.execute("SELECT synopsis FROM books WHERE id=?", (bookID,))
        row = cursor.fetchone()
        if row is not None:
            return str(row[0])   

    def getBookIMG(self, bookID: int) -> str:
        """
        Retrieve the image url address for a given book ID.
        """
        cursor = self.conn.execute("SELECT url FROM booksURL WHERE id=?", (bookID,))
        row = cursor.fetchone()
        if row is not None:
            return str(row[0])

    def getUserEmail(self, userID: int) -> str:
        """
        Retrieve the email address for a given user ID.
        """
        cursor = self.conn.execute("SELECT email FROM users WHERE id=?", (userID,))
        row = cursor.fetchone()
        if row is not None:
            return str(row[0])
    
    def getAdmType(self, userID: int) -> int:
        """
        Retrieve the type of an adm user.
        """
        cursor = self.conn.execute("SELECT type FROM adm WHERE id=?", (userID,))
        row = cursor.fetchone()
        if row is not None:
            return int(row[0])
        else:
            return 0
    
    def updateBookName(self, bookID: int, newName: str) -> None:
        """
        Update the name of a book with the given ID to the given new name.
        """
        try:
            self.conn.execute("UPDATE books SET name=? WHERE id=?", (newName, bookID))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Database.py: the book wih id {bookID} was not found in the database.\nError: {e}")
    
    def updateBookSynopsis(self, bookID: int, newSynopsis: str) -> None:
        """
        Update the synopsis of a book with the given ID to the given new synopsis.
        """
        try:
            self.conn.execute("UPDATE books SET synopsis=? WHERE id=?", (newSynopsis, bookID))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Database.py: the book wih id {bookID} was not found in the database.\nError: {e}")

    def updateBookAuthor(self, bookID: int, newAuthor: str) -> None:
        """
        Update the synopsis of a book with the given ID to the given new author.
        """
        try:
            self.conn.execute("UPDATE books SET author=? WHERE id=?", (newAuthor, bookID))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Database.py: the book wih id {bookID} was not found in the database.\nError: {e}")


    def updateBookIMG(self, bookID: int, url: str) -> None:
        """
        Update the image url addres of a book with a given ID to the given new url.
        """
        try:
            self.conn.execute("UPDATE booksURL SET url=? WHERE id=?", (url, bookID))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Database.py: the book wih id {bookID} was not found in the database.\nError: {e}")

    def updateUserEmail(self, userID: int, newEmail: str) -> None:
        """
        Update the email address for a given user ID.
        """
        try:
            self.conn.execute("UPDATE users SET email=? WHERE id=?", (newEmail, userID))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Database.py: the user wih id {userID} was not found in the database.\nError: {e}")

    # adm function
    def updateAdmType(self, userID: int, newType: int):
        """
        Update the role of an adm user.
        """
        try:
            self.conn.execute("UPDATE adm SET type=? WHERE id=?", (newType, userID))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Database.py: the user wih id {userID} was not found in the database.\nError: {e}")

    def addUser(self, userID: int, userEmail: str) -> None:
        """
        Add an user to the database.
        """
        try:
            self.conn.execute("INSERT INTO users (id, email) VALUES (?, ?)", (userID, userEmail))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise RuntimeError(f"Database.py: error at addUser: {e}.")

    def addBook(self, bookName: str, author: str, synopsis: str) -> None:
        """
        Add a new book to the database with the given name, author name,
        and synopsis.
        """
        try:
            self.conn.execute("INSERT INTO books (name, author, synopsis) VALUES (?, ?, ?)", (bookName, author, synopsis))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise RuntimeError(f"Database.py: error at addBook: {e}.")

    def addBookIMG(self, bookID: int, url: str) -> None:
        """
        Add a book image to the database.
        """
        try:
            self.conn.execute("INSERT INTO booksURL (id, url) VALUES (?, ?)", (bookID, url))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise RuntimeError(f"Database.py: error at addBookIMG: {e}.")
    
    # admin function
    def addAdm(self, userID: int, type: int, name: str) -> None:
        """
        Add an adm to the database.
        """
        try:
            self.conn.execute("INSERT INTO adm (id, type, name) values (?, ?, ?)", (userID, type, name))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise RuntimeError(f"Database.py: error at addAdm: {e}.")
    
    def removeBook(self, bookID: int) -> None:
        """
        Remove a book with the given ID from the database.
        """
        try:
            self.conn.execute("DELETE FROM books WHERE id=?", (bookID,))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Database.py: the book wih id {bookID} was not found in the database.\nError: {e}")

    def removeBookIMG(self, bookID: int) -> None:
        """
        Remove a book image with the given ID from the database.
        """
        try:
            self.conn.execute("DELETE FROM booksURL WHERE id=?", (bookID,))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Database.py: the book wih id {bookID} was not found in the database.\nError: {e}")
    
    def removeUser(self, user_id: int) -> None:
        """
        Remove an user with the given ID from the database.
        """
        try:
            self.conn.execute("DELETE FROM users WHERE id=?", (user_id,))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Database.py: the user wih id {user_id} was not found in the database.\nError: {e}")

    # admin function
    def removeAdm(self, user_id: int) -> None:
        """
        Remove an adm from the database.
        """
        try:
            self.conn.execute("DELETE FROM adm WHERE id=?", (user_id))
            self.conn.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Database.py: the user wih id {user_id} was not found in the database.\nError: {e}")

    def checkUserExists(self, userID: int) -> bool:
        """
        Check if an user with the given ID already exists in the database.
        """
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users WHERE id=?", (userID,))
        result = cur.fetchone()
        return result[0] > 0

