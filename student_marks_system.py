#Students marks tracker
#Lesedi Mohale
#26 April 2026


name = input("Please enter student name:\n").title()
num_of_subjects = int(input("Please enter the number of subjects taken:\n"))
info_dictionary = {}
total = 0

while num_of_subjects <= 0:
    print("Number of subjects must be greater than 0.")
    num_of_subjects = int(input("Please enter the number of subjects taken:\n"))

for i in range(num_of_subjects):
    
    subject_name = input("Please enter subject name:\n").title()
    marks = float(input("Please enter mark for that subject:\n"))
    
    info_dictionary.update({subject_name : marks})
    total += marks

average = round(total / num_of_subjects, 2)

best_subject = max(info_dictionary, key=info_dictionary.get)
best_mark = info_dictionary[best_subject]

worst_subject = min(info_dictionary, key=info_dictionary.get)
worst_mark = info_dictionary[worst_subject]

print("\n---- Student Report ----")
print("Name:", name)
for key, value in info_dictionary.items():
    print(f"Subject: {key}, Mark: {value} %" )
print(f"Average is: {average} %")
print(f"Result: {'Pass' if average >= 50 else 'Fail'}") 

print("\n---- Performance Summary ----")
print(f"Best Subject: {best_subject} ({best_mark} %)")
print(f"Worst Subject: {worst_subject} ({worst_mark} %)")