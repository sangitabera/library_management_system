class Book:
    def __init__(self, book_id: int, author: str, title: str):
        self.__book_id = book_id
        self.author = author
        self.title = title
        self.__is_available = True

    def get_book_id(self):
        return self.__book_id
    
    def is_available(self):
        return self.__is_available
    
    def set_availability(self, status: bool):
        self.__is_available = status

    def display_info(self):
        status = 'Available' if self.__is_available else 'Issued'
        print(f'Book ID: {self.__book_id}, Title: {self.title}, Author: {self.author} , Statues: {status}')

