from user import User

class staff(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.shifts = []

    def view_shifts(self, shifts):
        self.shifts = shifts 

    def raise_query(self, query):
        query.staff_id = self.user_id
        query.staff_name = self.name

