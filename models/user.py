from models.person import Person

class User(Person):
    def __init__(self, person_id : int, name:str):
        super().__init__(person_id, name)
        self.__issued_books = []

    def add_issued_books(self, book_id : int):
        self.__issued_books.append(book_id)

    def remove_issued_books(self, book_id: int):
        if book_id in self.__issued_books :
            self.__issued_books.remove(book_id)
        else:
            print(f'Book with ID:{book_id} is not in the list.')

    def get_issued_books(self):
        return self.__issued_books
    
    def display_info(self):
        print(f'User ID: {self.get_person_id()}, Name: {self.get_name()}, Issued Books: {self.__issued_books}')
