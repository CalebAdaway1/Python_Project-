from manager import Manager
from staff import Staff
from shift import Shift 
from query import Query 

class rota_manager:
    def __init__(self): 
        self.manager = []
        self.staff_members = []
        self.shifts = []
        self.queries = []

    def add_manager(self, manager):
        self.staff_members.append(manager)

    def add_staff(self, staff):
        self.staff_members.append(staff)

    def get_shift_for_staff(self, staff_id): 
        return [shift for shift in self.shifts if shift.employee_name == staff_id]

    def add_query(self, query):
        self.queries.append(query)

    def get_queries_for_manager(self, manager_id):
        return [query for query in self.queries if query.staff_id in [staff.user_id for staff in self.staff_members]]
