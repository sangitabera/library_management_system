class Validator:
    @staticmethod
    def validate_string(value: str):
        if not value.strip() :
            raise ValueError('Invalid string input, please modify it.')
        
    @staticmethod
    def validate_positive(value: int):
        if value <= 0:
            raise ValueError('Value must be positive.')