class Task:
    def __init__(self, title, description, due_date, assigned_to=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.assigned_to = assigned_to  
        
    def mark_complete(self):
        self.completed = True