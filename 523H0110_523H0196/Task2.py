import pandas as pd
from datetime import datetime, timedelta

# load data from CSV file
def load_data(file_path='students.csv'):
    try:
        data = pd.read_csv(file_path)

        data['Math'] = pd.to_numeric(data['Math'])
        data['CS'] = pd.to_numeric(data['CS'])
        data['Eng'] = pd.to_numeric(data['Eng'])
        return data
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return None

"""
Define these predicates based on your dataset, each predicate should return a 
boolean value for a given input.
"""
#  all scores are greater than or equal to 5
def is_passing(student):
    return student['Math'] >= 5 and student['CS'] >= 5 and student['Eng'] >= 5

# math score is greater than or equal to 9
def is_high_math(student):
    return student['Math'] >= 9

# math and cs score is less than 6
def is_struggling(student):
    return student['Math'] < 6 and student['CS'] < 6

# cs score is greater than math score
def improved_in_cs(student):
    return student['CS'] > student['Math']

def display_predicates_results(data):
    results = []
    for _, student in data.iterrows():
        result = {
            'StudentID': student['StudentID'],
            'StudentName': student['StudentName'],
            'is_passing': is_passing(student),
            'is_high_math': is_high_math(student),
            'is_struggling': is_struggling(student),
            'improved_in_cs': improved_in_cs(student)
        }
        results.append(result)
    
    print("\nResults of predicates on each student:")
    for result in results:
        print(f"Student {result['StudentID']} - {result['StudentName']}:")
        print(f"  - Passed all subjects: {result['is_passing']}")
        print(f"  - High math scores: {result['is_high_math']}")
        print(f"  - Is struggling: {result['is_struggling']}")
        print(f"  - Improved in cs : {result['improved_in_cs']}")
        print()

"""
Implement Python functions that evaluate whether each statement is true or false 
over your dataset. 
"""
# 2 Universal quantifications (e.g., ∀x P(x)) 

# All students passed all subjects
def all_students_passed(data):
    for _, student in data.iterrows():
        if not is_passing(student):
            return False
    return True

# All students have a math score higher than 3
def all_students_math_above_3(data):
    for _, student in data.iterrows():
        if not (student['Math'] > 3):
            return False
    return True

# 2 Existential quantifications (e.g., ∃x P(x))

# There exists a student who scored above 9 in math
def exists_student_high_math(data):
    for _, student in data.iterrows():
        if is_high_math(student):
            return True
    return False

# There exists a student who improved in CS over Math
def exists_student_improved_in_cs(data):
    for _, student in data.iterrows():
        if improved_in_cs(student):
            return True
    return False

# 2 Combined/nested statements (e.g., ∀x ∃y Q(x, y))

def for_every_student_exists_subject_above_6(data):
    for _, student in data.iterrows():
        if student['Math'] <= 6 and student['CS'] <= 6 and student['Eng'] <= 6:
            return False
    return True

# For every student scoring below 6 in Math, there exists a subject where they scored above 6
def for_every_student_with_low_math_exists_subject_above_6(data):
    for _, student in data.iterrows():
        if student['Math'] < 6:
            if student['CS'] <= 6 and student['Eng'] <= 6:
                return False
    return True

# Function evaluate quantified statements
def evaluate_quantified_statements(data):
    
    print("\nEvaluate quantified statements:")
    
    print("\n1. Universal quantifications (e.g., ∀x P(x)):")
    print(f"- All students passed: {all_students_passed(data)}")
    print(f"- All students have math scores higher than 3: {all_students_math_above_3(data)}")
    
    print("\n2. Existential quantifications (e.g., ∃x P(x)):")
    print(f"- There exists a student whose math score is above 9: {exists_student_high_math(data)}")
    print(f"- There is a student whose cs score is higher than his math score.: {exists_student_improved_in_cs(data)}")
    
    print("\n3. 2 Combined/nested statements (e.g., ∀x ∃y Q(x, y)):")
    print(f"- For every student, there exists a subject in which they score above 6: {for_every_student_exists_subject_above_6(data)}")
    print(f"- For every student who scores below 6 in math, there exists one subject in which they score above 6: {for_every_student_with_low_math_exists_subject_above_6(data)}")


"""
Write Python functions to evaluate the negation of the quantified statements 
above and explain their meaning in plain English. 
"""
# The negation of the quantified statements

# Negation of 'All students passed all subjects'
# There exists at least one student who did not pass all subjects
def not_all_students_passed(data):
    for _, student in data.iterrows():
        if not is_passing(student):
            return True
    return False

# Negation of 'All students have math scores higher than 3'
# There exists at least one student whose math score is less than or equal to 3
def not_all_students_math_above_3(data):
    for _, student in data.iterrows():
        if student['Math'] <= 3:
            return True
    return False

# Negation of Existential Quantifications

# Negation of 'There exists a student who scored above 9 in math"
# All students have math scores less than 9.
def not_exists_student_high_math(data):
    for _, student in data.iterrows():
        if is_high_math(student):
            return False
    return True

# Negation of 'There exists a student who improved in CS over Math'
# All students have CS scores less than or equal to their Math scores.
def not_exists_student_improved_in_cs(data):
    for _, student in data.iterrows():
        if improved_in_cs(student):
            return False
    return True

# Negation of Combined/Nested Quantifications

# Negation of 'For every student, there exists a subject in which they scored above 6
# There exists at least one student who scored 6 or lower in all subjects.
def not_for_every_student_exists_subject_above_6(data):
    for _, student in data.iterrows():
        if student['Math'] <= 6 and student['CS'] <= 6 and student['Eng'] <= 6:
            return True
    return False

# Negation of 'For every student scoring below 6 in Math, there exists a subject where they scored above 6
# There exists at least one student who has a Math score below 6 and also scored 6 or lower in all other subjects.
def not_for_every_student_with_low_math_exists_subject_above_6(data):
    for _, student in data.iterrows():
        if student['Math'] < 6:
            if student['CS'] <= 6 and student['Eng'] <= 6:
                return True
    return False

# Function evaluate the negation of the quantified statements
def evaluate_negated_statements(data):
    print("\nEvaluate the negation of the quantified statements :")
    
    # 1. Negation of Universal Quantifications
    print("\n1. Negation of Universal Quantifications:")

    print(f"- Negation of 'All students passed all subjects': {not_all_students_passed(data)}")
    print("  Meaning: There exists at least one student who did not pass all subjects.")

    print(f"- Negation of 'All students have math scores higher than 3': {not_all_students_math_above_3(data)}")
    print("  Meaning: There exists at least one student whose math score is less than or equal to 3.")

    # 2. Negation of Existential Quantifications
    print("\n2. Negation of Existential Quantifications:")

    print(f"- Negation of 'There exists a student who scored above 9 in math': {not_exists_student_high_math(data)}")
    print("  Meaning: All students have math scores less than 9.")

    print(f"- Negation of 'There exists a student who improved in CS over Math': {not_exists_student_improved_in_cs(data)}")
    print("  Meaning: All students have CS scores less than or equal to their Math scores.")

    # 3. Negation of Combined/Nested Quantifications
    print("\n3. Negation of Combined/Nested Quantifications:")

    print(f"- Negation of 'For every student, there exists a subject in which they scored above 6': {not_for_every_student_exists_subject_above_6(data)}")
    print("  Meaning: There exists at least one student who scored 6 or lower in all subjects.")

    print(f"- Negation of 'For every student scoring below 6 in Math, there exists a subject where they scored above 6': {not_for_every_student_with_low_math_exists_subject_above_6(data)}")
    print("  Meaning: There exists at least one student who has a Math score below 6 and also scored 6 or lower in all other subjects.")


if __name__ == "__main__":
    data = load_data()
    if data is not None:
        print("Data from file CSV:")
        print(data.head(21))
        
        # Display results
        # display_predicates_results(data)

        # evaluate quantified statements
        evaluate_quantified_statements(data)

        # evaluate negated statements
        evaluate_negated_statements(data)