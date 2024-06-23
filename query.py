class Query:
    def __init__(self, query_id, staff_id, query_text):
        self.query_id = query_id
        self.staff_id = staff_id
        self.query_text = query_text
        self.response = None