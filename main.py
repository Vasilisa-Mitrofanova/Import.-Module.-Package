from application import salary, people
import datetime

if __name__ == '__main__':
    print(f"Текущая дата: {datetime.date.today()}")
    salary.calculate_salary()
    people.get_employees()