from .models import Employee, ChatHistory

def create_employee(db, full_name, email, password, position, department):
    new_employee = Employee(
        full_name=full_name,
        email=email,
        password=password,
        position=position,
        department=department
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_employee_by_email(db, email):
    employee = db.query(Employee).filter(Employee.email == email).first()
    if not employee:
        raise ValueError("Employee with the given email does not exist.")
    return employee