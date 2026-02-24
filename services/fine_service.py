from datetime import datetime

class FineService:
    def __init__(self, fine_per_day=5):
        self.fine_per_day = fine_per_day

    def calculate_fine(self, due_date):
        today = datetime.now()
        if today > due_date :
            days_late = (today - due_date).days
            fine_amount = days_late * self.fine_per_day
            return fine_amount
        return 0