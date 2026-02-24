from models.person import Person

class Admin(Person):
    def display_info(self):
        print(f'User ID: {self.get_person_id()}, Name: {self.get_name()}')