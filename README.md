# 📊 Student Marks System (Python)

A command-line Python application that collects, processes, and evaluates student academic performance across multiple subjects.

This project demonstrates fundamental programming concepts such as data structures, functions, input validation, and basic data analysis.

---

## 📌 Project Overview

This project is a student performance analysis system written in Python. It allows users to input subject marks, calculate averages, and analyze academic performance. 

---

## 🎯 Project Purpose

The goal of this project is to simulate a simple academic grading system that:

 - Stores student subject marks
 - Calculates overall performance
 - Identifies strongest and weakest subjects
 - Assigns a final grade based on average performance

It was built as part of my learning journey in Python to strengthen problem-solving and structured programming skills.

---

## ⚙️ Features
- Input student name and number of subjects
- Dynamic subject and mark entry
- Input validation for:
   - Number of subjects (> 0)
   - Marks (0–100 range)
- Automatic calculation of:
   - Average mark
   - Best performing subject
   - Worst performing subject
- Grade classification system:
   - Distinction (A)
   - Second Class (B)
   - Pass (C)
   - Weak Pass (D)
   - Fail (F)
- Clean, structured output report
  
---

## 🧠 Key Concepts & Skills Demonstrated

This project demonstrates understanding of:

- Dictionaries for strutured data storage
- Loops and iteration
- Aggregation and calculations (averages)
- Use of max() and min() with key functions
- Input validation and user interaction
    

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
   - Assign grade based on average score
4. Output Phase
   - Display a structured performance report

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

## 📁 Project Structure

student-marks-system/
│
├── marks.py        # Main program logic
└── README.md       # Project documentation

---

## ▶️ How to Run the Project

Clone the repository:
git clone https://github.com/Sedi-dev/student-marks-system.git

Navigate into the project folder:
cd student-marks-system

Run the program:
python marks.py 

---

## 💡 Learning Outcome

This project improved my ability to structure and analyze data using dictionaries, as well as apply built-in Python functions for efficient data processing.
- How to structure a program using multiple functions
- How to use dictionaries to model real-world data
- How to perform calculations on grouped data
- How to validate and sanitize user input
- How to design a clean output/report system

---

 ## 📌 Challenges Faced

One of the main challenges was designing a system that could handle multiple subjects dynamically while still producing accurate summaries. This was solved using dictionary-based storage and built-in Python functions like sum(), max(), and min(). 

---

## 🚀 Future Improvements
- Add file saving/loading for student records
- Support multiple students in one system
- Add GUI version (Tkinter or web-based interface)
- Export results as PDF report cards
- Add ranking system for multiple students

---

## ⭐ Project Purpose

This project was built as part of my Computer Science learning journey to apply programming concepts in a structured, real-world simulation.

It demonstrates my ability to:

- Break down problems logically
- Design modular programs
- Work with structured data
- Build functional Python applications

---


