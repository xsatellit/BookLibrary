# Here are all functions that an admin user or other special user should use to manage the library

from database.Database import DatabaseFunctions
from helpers.jsonHandler import jsonHandler
from functions.default.SearchFiles import SearchFiles

# Add the remove, update and insert of the jsonHandler -> Maybe I'll have to create the functions inside the class :(
class Admin:

    def __init__(self) -> None:
        self.database = DatabaseFunctions()
        self.json = jsonHandler()

    def checkAdmin(self, userID) -> int:
        user_type = self.database.getAdmType(userID)
        return user_type
    
    def getRole(self, role: int) -> dict:
        roles = {
            1: "Dona",
            2: "Administradora"
        }

        return roles[role]

    def getAllAdmin(self) -> dict:
        return self.database.getAllAdm()
    
    def getBookID(self, bookTitle):
        return self.database.getBookID(bookTitle)
    
    def addBook(self, bookName: str, author: str, synopsys: str) -> str:
        try:
            self.database.addBook(bookName, author, synopsys)
            return "O livro foi adicionado no banco de dados."
        except RuntimeError as e:
            return f"Não foi possível adicionar o livro no banco de dados. Erro ocorrido: {e}"
    
    def addBookJson(self, book_title: str, book_author: str, book_id: int, book_command: str, book_gender: str) -> None:
        try:
            value = {
                "ID": book_id,
                "Telegram": f"{book_command} - {book_title} - {book_author}",
                "Name": f"{book_command}"
            }
            self.json.add_key(book_gender, book_title, value)
            return "O livro foi adicionado no banco de dados."
        except RuntimeError as e:
            return f"Não foi possível adicionar o livro no arquivo json. Erro ocorrido: {e}"
        except TypeError as e:
            return f"Não foi possível adicionar o livro no arquivo json. Erro ocorrido: {e}"
        except ValueError as e:
            return f"Não foi possível adicionar o livro no arquivo json. Erro ocorrido: {e}"

    def addBookIMG(self, bookID: int, url: str) -> str:
        try:
            self.database.addBookIMG(bookID, url)
            return "A capa do livro foi adicionada no banco de dados."
        except RuntimeError as e:
            return f"Não foi possível adicionar a capa no banco de dados. Erro ocorrido: {e}"
    
    def addAdmin(self, userID: int, role: int, name: str) -> str:
        try:
            self.database.addAdm(userID, role, name)
            return "O administrador foi adicionado ao banco de dados."
        except RuntimeError as e:
            return f"Não foi possível adicionar o administrador ao banco de dados. Erro ocorrido: {e}"
    
    def updateBookName(self, bookID: int, newName: str) -> str:
        try:
            self.database.updateBookName(bookID, newName)
            book_name = self.json.getKeyForSubkey("ID", bookID)
            book_gender = self.json.getMasterkeyForKey(book_name)
            self.json.updateKey(book_gender, book_name, newName)
            return "O nome do livro foi atualizado no banco de dados."
        except ValueError as e:
            return f"Não foi possível atualizar o livro no banco de dados. Erro ocorrido: {e}"
    
    def updateBookAuthor(self, bookID: int, newAuthor: str) -> str:
        try:
            self.database.updateBookAuthor(bookID, newAuthor)
            return "O autor do livro foi atualizado no banco de dados."
        except ValueError as e:
            return f"Não foi possível atualizar o livro no banco de dados. Erro ocorrido: {e}"
    
    def updateBookSynopsis(self, bookID: int, newSynopsis: str) -> str:
        try:
            self.database.updateBookSynopsis(bookID, newSynopsis)
            return "A sinopse do livro foi atualizada no banco de dados."
        except ValueError as e:
            return f"Não foi possível atualizar o livro no banco de dados. Erro ocorrido: {e}"
    
    def updateBookIMG(self, bookID: int, newUrl: str) -> str:
        try:
            self.database.updateBookIMG(bookID, newUrl)
            return "A capa do livro foi atualizada no banco de dados."
        except ValueError as e:
            return f"Não foi possível atualizar a capa no banco de dados. Erro ocorrido: {e}"
    
    def updateBookJson(self, bookID: int, newValue: str) -> str:
        try:
            book_name = self.json.getKeyForSubkey("ID", bookID)
            book_gender = self.json.getMasterkeyForKey(book_name)
            self.json.updateValue(book_gender, book_name, "Name", newValue)
            return "O comando do livro foi atualizado" 
        except RuntimeError as e:
            return f"Não foi possível atualizar o comando do livro no arquivo json. Erro ocorrido: {e}"
        except TypeError as e:
            return f"Não foi possível atualizar o comando do livro no arquivo json. Erro ocorrido: {e}"
        except ValueError as e:
            return f"Não foi possível atualizar o comando do livro no arquivo json. Erro ocorrido: {e}"
    
    def updateAdminType(self, user_id: str, newtype: int) -> str:
        try:
            self.database.updateAdmType(user_id, newtype)
            return "O cargo foi atualizado com sucesso."
        except ValueError as e:
            return f"Não foi possível atualizar o cargo no banco de dados. Erro ocorrido: {e}"

    def removeBook(self, bookID) -> str:
        try:
            self.database.removeBook(bookID)
            self.database.removeBookIMG(bookID)
            book_name = self.json.getKeyForSubkey("ID", bookID)
            book_gender = self.json.getMasterkeyForKey(book_name)
            self.json.remove(book_gender, book_name)
            SearchFiles().removeFile(book_name, "pdf")
            SearchFiles().removeFile(book_name, "mobi")
            SearchFiles().removeFile(book_name, "epub")
            return "O livro foi removido da biblioteca."
        except ValueError as e:
            return f"Não foi possível remover o livro do banco de dados. Erro ocorrido: {e}"
        except RuntimeError as e:
            return f"Não foi possível remover o livro do banco de dados. Erro ocorrido: {e}"

    
    def removeBookIMG(self, bookID) -> str:
        try:
            self.database.removeBookIMG(bookID)
            return "A capa foi removida do banco de dados."
        except ValueError as e:
            return f"Não foi possível remover a capa do banco de dados. Erro ocorrido: {e}"
    
    def removeAdmin(self, user_id: str) -> str:
        try:
            self.database.removeAdm(user_id)
            return "O cargo foi removido com sucesso."
        except ValueError as e:
            return f"Não foi possível remover o cargo no banco de dados. Erro ocorrido: {e}"


