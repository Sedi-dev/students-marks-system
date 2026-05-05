#Students marks tracker
#Lesedi Mohale
#26 April 2026

import json
import os

def get_student_info():
    
    name = input("Please enter student name:\n").title()
    num_of_subjects = int(input("Please enter the number of subjects taken:\n"))
    subjects = {}
    
    while num_of_subjects <= 0:
        print("Number of subjects must be greater than 0.")
        num_of_subjects = int(input("Please enter the number of subjects taken:\n"))
        
    for _ in range(num_of_subjects):
    
        subject_name = input("Please enter subject name:\n").title()
        mark = float(input("Please enter mark for that subject:\n"))
        
        while mark < 0 or mark > 100:
            print("Invalid mark. Must be between 0 and 100.")
            mark = float(input("Please enter mark for that subject:\n"))
            
        subjects[subject_name] = mark
    
    return name, subjects

def calc_results(subjects):
    
    total = sum(subjects.values())
    average = round(total / len(subjects), 2)

    best_subject = max(subjects, key=subjects.get)
    worst_subject = min(subjects, key=subjects.get)
    
    return average, best_subject, subjects[best_subject], worst_subject, subjects[worst_subject]

def get_grade(average):
    
    if average >= 75:
        return "Distinction (A)"
    elif average >= 70:
        return "Second Class (B)" 
    elif average >= 60:
        return "Pass (C)"
    elif average >= 50:
        return "Weak Pass (D)" 
    else:
        return "Fail (F)"

def display_report(name, subjects, average, grade, best_subject, best_mark, worst_subject, worst_mark):
    
    print("\n---- Student Report ----")
    print("Name:", name)
    for subject, mark in subjects.items():
        print(f"Subject: {subject}, Mark: {mark}%" )
        
    print(f"Average: {average}%")
    print(f"Result: {grade}") 

    print("\n---- Performance Summary ----")
    print(f"Best Subject: {best_subject} ({best_mark}%)")
    print(f"Worst Subject: {worst_subject} ({worst_mark}%)")
    
def save_to_file(name, subjects, average, grade, best_subject, best_mark, worst_subject, worst_mark):
    """ Save student report to a textfile. """
    
    with open("student_report.txt", "a") as f:
        
        f.write("\n" + "~"*40 + "\n")   #separator for each report
        f.write("\n---- Student Report ----\n")
        f.write(f"Name: {name}\n\n")
        
        for subject, mark in subjects.items():
            f.write(f"{subject}: {mark}%\n")
    
        f.write(f"Average: {average} %\n")
        f.write(f"Result: {grade}\n")
    
        f.write("\n---- Performance Summary ----\n")
        f.write(f"Best Subject: {best_subject} ({best_mark}%)\n")
        f.write(f"Worst Subject: {worst_subject} ({worst_mark}%)\n")        
        
def save_all_students(student_list):
    """ Save students' reports to .json . """
    
    with open("student_data.json", "w") as f:
        json.dump(student_list, f, indent = 4)
    
    
def load_students():
    """ Load all students from JSON file. Returns empty list if file doesn't exist. """
    
    if os.path.exists("student_data.json"):
        with open("student_data.json", "r") as f:
             
            return json.load(f) 
    else:
        return []  
    
def add_new_students():
    """ Get student info, calculate results, and return the student dictionary """
    
    name, subjects = get_student_info()
    avg, best, best_mark, worst, worst_mark = calc_results(subjects)
    grade = get_grade(avg)
    
    display_report(name, subjects, avg, grade, best, best_mark, worst, worst_mark)
    
    save_to_file(name, subjects, avg, grade, best, best_mark, worst, worst_mark)
    
    new_student = {"Name" : name, 
                   "Subjects" : subjects, 
                   "Average" : avg, 
                   "Grade" : grade, 
                   "Best Subject" : best, 
                   "Best Mark" : best_mark, 
                   "Worst Subject" : worst, 
                   "Worst Mark" : worst_mark }
    
    return new_student

def display_all_students(student_list):
    """ Display all saved students. """
    
    if not student_list:
        print("\n❌ No students found. Please add a student first.\n")
        return
    
    print("\n" + "="*50)
    print("ALL SAVED STUDENTS")
    print("="*30)
    
    for i, student in enumerate(student_list, 1):
        
        print(f"\n📚 Student {i}: {student['Name']} ")
        print(f" Average: {student['Average']}%")
        print(f" Grade: {student['Grade']}")
        print(f" Best: {student['Best Subject']} ({student['Best Mark']})%")
        print(f" Worst: {student['Worst Subject']} ({student['Worst Mark']})%")
        print("~" * 30)
    
    return    
    
def main():
    
    all_students = load_students()
    
    if not all_students:
        print("No existing data found. Starting fresh. ")
    else:
        print(f"Loaded {len(all_students)} existing student(s).")
    
    while True:
        print("\n" + "="*40)
        print("STUDENT MARKS CAPTURING SYSTEM")
        print("="*40)
        print("1. Add a new student")
        print("2. View all students")
        print("3. Exit")
        print("="*40)
        
        choice = input("Choose an option (1-3):\n")
        
        if choice == "1":
            print("\n---- Add New Student ----")
            
            new_student = add_new_students()
            all_students.append(new_student)
            save_all_students(all_students)
            
            print(f"\n✅ {new_student['Name']} has been added!")
            print(f"📁 Total students in database: {len(all_students)}")
        
        elif choice == "2":
            print("\n---- View All Students ----")
            display_all_students(all_students)
        
        elif choice == "3":
            print("\nExiting Program. Goodbye!")
            break
        
        else:
            print("\n Invalid choice. Please enter 1, 2, or 3.")
    
    
if __name__=='__main__':
    main()