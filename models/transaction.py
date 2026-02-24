from datetime import datetime, timedelta

class Transaction:
    def __init__(self, transaction_id : int, user_id : int, book_id : int):
        self.__transaction_id = transaction_id
        self.__user_id = user_id
        self.book_id = book_id
        self.issue_date = datetime.now()
        self.due_date = self.issue_date + timedelta(days=15)
        self.return_rate = None
        self.fine_amount = 0

    def get_user_id(self):
        return self.__user_id 
    
    def display_info(self):
        print(f'User ID: {self.__user_id}, Book ID: {self.book_id}, Transaction ID: {self.__transaction_id}, Fine Amount: {self.fine_amount}')