import csv
import pandas as pd
import random
from datetime import datetime, timedelta

# Create a dataset of students with random data
def create_dataset(file_path='students.csv'):
    students = []

    for i in range(1, 21):
        student_id = f"SV{i:03d}"
        
        first_names = ["Nam", "Minh", "Hoa", "Lan", "Anh", "Tuan", "Linh", "Hai", "Mai", "Duc"]
        last_names = ["Nguyen", "Tran", "Le", "Pham", "Hoang", "Vo", "Dang", "Bui", "Do", "Dinh"]
        student_name = f"{random.choice(last_names)} {random.choice(first_names)}"
        
        start_date = datetime(2000, 1, 1)
        end_date = datetime(2005, 12, 31)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_days)
        day_of_birth = random_date.strftime("%d/%m/%Y")
        
        if i <= 5:
            math = round(random.uniform(8.0, 10.0), 1)
            cs = round(random.uniform(8.0, 10.0), 1)
            eng = round(random.uniform(8.0, 10.0), 1)
        elif i <= 10:
            math = round(random.uniform(9.0, 10.0), 1)
            cs = round(random.uniform(5.0, 8.0), 1)
            eng = round(random.uniform(5.0, 8.0), 1)
        elif i <= 15: 
            math = round(random.uniform(4.0, 7.0), 1)
            cs = round(math + random.uniform(1.0, 3.0), 1)
            if cs > 10.0:
                cs = 10.0
            eng = round(random.uniform(5.0, 9.0), 1)
        else:
            math = round(random.uniform(3.0, 5.5), 1)
            cs = round(random.uniform(3.0, 5.5), 1)
            eng = round(random.uniform(5.0, 9.0), 1)
        
        students.append([student_id, student_name, day_of_birth, math, cs, eng])

    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["StudentID", "StudentName", "DayOfBirth", "Math", "CS", "Eng"])
        writer.writerows(students)

    print(f"Create a {file_path} with records.")
    return file_path

create_dataset('students.csv')
