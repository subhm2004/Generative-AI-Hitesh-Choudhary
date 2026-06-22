# ============================================================
# FILE: day_2.py
# TOPIC: Dictionary, min/max/sum, list comprehension
# FOLDER: challenges/02_data_handling
# CHALLENGE DAY: Day 2
# ============================================================
# Yeh challenge sikhata hai:
# - Dictionary = student name -> marks store karna
# - while loop se multiple students ka data collect karna
# - max(), min(), sum() built-in functions statistics ke liye
# - List comprehension se filter karna (topper/bottomer nikalna)
# - .items() = dictionary ke key-value pairs par loop
# ============================================================

"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

def collect_student_data():
    students = {}  # khali dictionary - name: marks store hoga

    while True:
        name = input("Enter the student name or done to exit: ").strip()
        
        # "done" type kiya to input loop band karo
        if name.lower() == "done":
            break
        # Duplicate name check - dictionary mein key already hai?
        if name in students:
            print("Student already exists")
            continue  # next iteration, dobara naam poocho

        try:
            marks = float(input(f"Enter marks for {name}: "))
            students[name] = marks  # dictionary mein add karo
        except ValueError:
            print("Please enter a valid number for marks")

    return students


def display_report(students):
    if not students:
        print("No student data ❌")
        return
    
    # students.values() = sirf marks ki list
    marks = list(students.values())
    max_score = max(marks)   # sabse zyada marks
    min_score = min(marks)   # sabse kam marks
    average = sum(marks) / len(marks)  # average = total / count

    # List comprehension = ek line mein filter + list banao
    # Jinka score == max_score woh sab topper hain
    topper = [name for name, score in students.items() if score == max_score ]
    bottomer = [name for name, score in students.items() if score == min_score ]

    print("\n Students marks report 🗓️")
    print("-" * 30)
    print(f"Total students: {len(students)}")
    print(f"average marks for students: {average:.2f}")  # :.2f = 2 decimal places
    # ', '.join(list) = list ko comma-separated string mein convert
    print(f"Highest marks : {max_score} by {', '.join(topper)}")
    print(f"lowest marks : {min_score} by {', '.join(bottomer)}")

    print("-" * 30)
    print("Detailed Marks 🗓️")
    # .items() = har student ka naam aur marks
    for name, score in students.items():
        print(f" - {name}: {score}")


students = collect_student_data()
display_report(students)
