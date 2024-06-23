from manager import Manager
from staff import Staff
from shift import Shift
from rota_manager import RotaManager
from query import Query

def main():
    rota_manager = RotaManager()

    manager = Manager(1, "Tash", "Tash@example.com")
    rota_manager.add_manager(manager)

    staff = Staff(2, "Caleb", "Caleb@example.com")
    rota_manager.add_staff(staff)
    manager.queries = rota_manager.queries  # To allow manager to respond to queries

    shift = Shift(1, "Caleb", "20-06-2024 09:00", "20-06-2024 17:00", "Support tills + self checkout")
    manager.add_shift(shift)
    rota_manager.shifts.append(shift)

    staff.view_shifts(rota_manager.get_shift_for_staff(staff.user_id))

    query = Query(1, staff.user_id, "I am still waiting for my new uniform, when will this be ready for me?")
    staff.raise_query(query)
    rota_manager.add_query(query)

    manager.respond_to_query(query.query_id, "It is due in on Monday")

    # Display the shifts for the staff
    for shift in staff.shifts:
        print(f"Shift ID: {shift.shift_id}, Tasks: {shift.tasks}")

    # Display the query and response
    for query in rota_manager.queries:
        print(f"Query: {query.query_text}, Response: {query.response}")

if __name__ == '__main__':
    main()

