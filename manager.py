from user import User

class manager(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.shifts = []
        self.queries = []
        
    def add_shift(self, shift):
        self.shifts.append(shift)

    def remove_shift(self, shift_id):
        self.shifts = [shift for shift in self.shifts if shift.shift_id != shift_id]

    def respond_to_query(self, query_id, response):
        for query in self.queries:
            if query.query_id == query_id:
                query.response = response  
