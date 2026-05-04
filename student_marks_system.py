#Students marks tracker
#Lesedi Mohale
#26 April 2026

def get_student_info():
    
    name = input("Please enter student name:\n").title()
    num_of_subjects = int(input("Please enter the number of subjects taken:\n"))
    subjects = {}
    
    while num_of_subjects <= 0:
        print("Number of subjects must be greater than 0.")
        num_of_subjects = int(input("Please enter the number of subjects taken:\n"))
        
    for i in range(num_of_subjects):
    
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

def display_report(name, subjects, average, best_subject, best_mark, worst_subject, worst_mark):
    
    print("\n---- Student Report ----")
    print("Name:", name)
    for key, value in subjects.items():
        print(f"Subject: {key}, Mark: {value} %" )
        
    print(f"Average is: {average} %")
    print(f"Result: {get_grade(average)}") 

    print("\n---- Performance Summary ----")
    print(f"Best Subject: {best_subject} ({best_mark} %)")
    print(f"Worst Subject: {worst_subject} ({worst_mark} %)")
    
def main():
    
    name, subjects = get_student_info()
    avg, best, best_mark, worst, worst_mark = calc_results(subjects)
    
    display_report(name, subjects, avg, best, best_mark, worst, worst_mark)
  
    
if __name__=='__main__':
    main()
