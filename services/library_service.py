from models.book import Book
from models.user import User
from models.person import Person
from models.transaction import Transaction
from services.fine_service import FineService
from utils.exceptions import *
from utils.id_generator import IDGenerator


class LibraryService:
    def __init__(self):
        self.books = []
        self.users = []
        self.__transactions = []
        self.fine_service = FineService()


    def add_book(self, title, author):
        book_id = IDGenerator.generate_id()
        book = Book(book_id, title, author)
        self.books.append(book)

    def register_user(self, name):
        user_id = IDGenerator.generate_id()
        user = User(user_id, name)
        self.users.append(user)

    def display_books(self):
        for book in self.books:
            book.display_info()

    def __find_book(self, book_id):
        for book in self.books :
            if book.book_id == book_id :
                return book
        raise BooKNotFoundError('Book not found.')
    
    def __find_user(self, user_id):
        for user in user_id:
            if self.person_id == user_id :
                return user
        raise UserNotFoundError('User not found.')


    def issue_book(self, user_id, book_id):
        book = self.__find_book(book_id)
        user = self.__find_user(user_id)

        if not book.is_available():
            raise BooKNotAvailableError('Book already issued.')
        book.set_availability(False)
        user.add_issued_book(book_id)

        transaction = Transaction(IDGenerator.generate_id(), user_id, book_id)
        self.__transactions.append(transaction)

    
    def return_book(self, user_id, book_id):
        book = self.__find_book(book_id)
        user = self.__find_user(user_id)

        book.set_availability(True)
        user.remove_issued_book(book_id)

        for t in self.__transactions:
            if t.get_book_id == book_id and t.get_user_id == user_id :
                fine = self.fine_service.calculate_fine(t.due_date())
                t.set_fine(fine)
                print(f'Fine: ${fine}')
                