class IDGenerator:
    __current_id = 1

    @classmethod
    def generate_id(cls):
        id = cls.__current_id
        cls.__current_id += 1
        return id