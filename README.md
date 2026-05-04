# 📊 Student Marks System (Python)

A command-line Python application that collects student subject marks, calculates performance, and generates a structured report.

This project focuses on problem-solving, data handling, and building clean, modular code.

---

## 📌 Project Overview

This project simulates a simple grading system. It allows users to input subject marks, calculate averages, and generate a structured performance report.

---

## ⭐ Project Purpose

This project was built as part of my Computer Science learning journey to apply programming concepts in a structured, real-world simulation.

It demonstrates my ability to:

- Break down problems logically
- Design modular programs
- Work with structured data
- Build functional Python applications

---

## ⚙️ Features

- Input student name and number of subjects  
- Dynamic subject and mark entry  
- Input validation:
  - Number of subjects (> 0)  
  - Marks (0–100 range)  
- Calculates:
  - Average mark  
  - Best performing subject  
  - Worst performing subject  
- Grade classification system (A–F scale)  
- Displays a clean, structured report  
- Saves report to a text file (`student_report.txt`)  
- Appends multiple student reports  

---


## 🧠 Key Concepts & Skills Demonstrated

This project demonstrates understanding of:

- Dictionaries for structured data storage
- Loops and iteration
- Aggregation and calculations (averages)
- Use of max() and min() with key functions
- Input validation and user interaction

---

## 🧠 How It Works

The program follows a simple structured flow:

1. Input Phase
   - Collect student name
   - Collect number of subjects
   - Collect subject names and marks
2. Processing Phase
   - Store data in a dictionary (subject → mark)
   - Calculate total and average
   - Determine best and worst subjects
3. Evaluation Phase
   - Assign grade based on average mark
4. Output Phase
   - Display a structured performance report
5. File Handling
   - Saves results to a text file

---

## 🧮 Grading System

| Average Score | Grade            |
| ------------- | ---------------- |
| 75 – 100      | Distinction (A)  |
| 70 – 74       | Second Class (B) |
| 60 – 69       | Pass (C)         |
| 50 – 59       | Weak Pass (D)    |
| Below 50      | Fail (F)         |

---

## 🛠️ Technologies Used

- Python 3
- Built-in data structures (dict, list)
- Conditional statements
- Functions for modular design

---

## 📦 Dependencies
No external libraries required — runs with Python standard library only.

### Requirements
- Python 3.6 or higher
- No pip install needed

---

## 📁 Project Structure

student-marks-system/
│
├── student_marks_system.py   # Main program logic
└── README.md                 # Project documentation

---

## ▶️ How to Run the Project

Clone the repository:
git clone https://github.com/Sedi-dev/student-marks-system.git

Navigate into the project folder:
cd student-marks-system

Run the program:
python3 student_marks_system.py 

---

## 💡 Learning Outcome

This project improved my ability to structure and analyze data using dictionaries, as well as apply built-in Python functions for efficient data processing. I learnt:
- How to structure a program using multiple functions
- How to use dictionaries to model real-world data
- How to perform calculations on grouped data
- How to validate and sanitize user input
- How to design a clean output/report system
- Writing data to files and managing persistence

---

 ## 📌 Challenges Faced

One of the main challenges was designing a system that could handle multiple subjects dynamically while still producing accurate summaries. This was solved using dictionary-based storage and built-in Python functions like sum(), max(), and min(). 

---

## 🚀 Future Improvements

- Support multiple students in one system
- Add GUI version (Tkinter or web-based interface)
- Export results as PDF report cards
- Add ranking system for multiple students
- Store and retrieve data from a database

---

## 👨🏻‍💻 Program Demo

![Student marks system running](https://github.com/user-attachments/assets/df597fbd-a833-4ea5-8070-602d052afb11)

![Invalid subject number](https://github.com/user-attachments/assets/b964169d-e950-46e6-91ee-4cae76e1a770)

![Input validation for marks](https://github.com/user-attachments/assets/557dbd49-d856-4438-83aa-a39578051a0a)


![student.txt](https://github.com/user-attachments/assets/57b7fd68-1d28-4ed5-8164-24e460e5c8b5)

---

## ⭐ Final Note

This project reflects my approach to learning:
building complete, functional programs to apply and reinforce core concepts.

---

Last updated: May 2026
