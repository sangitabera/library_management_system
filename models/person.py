class Person:
    def __init__(self, person_id : int, name : str):
        self.__person_id = person_id
        self.__name = name

    def get_person_id(self):
        return self.__person_id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name : str):
        if not name.strip():
            raise ValueError('Name cannot be empty.')
        self.__name = name

    def display_info(self):
        print(f'ID: {self.__person_id} and Name is: {self.__name}')