from db.crud import get_employee_by_email
from db.db_auth import SessionLocal
from rag.confluence_loader import get_pages_from_space

db = SessionLocal()

email = input("Enter your email to show an available documentation: ")

try:
    employee = get_employee_by_email(db, email)
except ValueError as e:
    print(e)
    exit(1)

available_pages = get_pages_from_space(employee.department)
print([page['title'] for page in available_pages])