import application.db.people
from application.salary import calculate_salary
from datetime import datetime
from pycalc3.calculator import Calculator

current_date = datetime.now()

if __name__ == '__main__':
    application.db.people.get_employees()
    calculate_salary()
    print(current_date)

