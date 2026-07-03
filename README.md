# 📊 Student Marks System (Python)

A modular Python application that manages student academic records, calculates performance statistics, and stores data persistently using JSON, and generates visual analytics.

This project focuses on problem-solving, data handling, and building clean, modular programs that simulate real-world systems. This project evolved from a simple grading calculator into a multi-student management system with persistent storage and graphical reporting.

---

## 📌 Project Overview

This project simulates a simple grading system. It allows users to input subject marks, calculate averages, and generate a structured performance report.

The system has been extended to include persistent storage and multi-student support, making it closer to a real-world application.

This project now allows users to generate graphical analytics.

---

## ⭐ Project Purpose

This project was built as part of my Computer Science learning journey to apply programming concepts in a structured, practical context.

It demonstrates my ability to:

- Break down problems logically
- Design modular programs
- Work with structured data
- Build complete, functional Python applications

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
- JSON-based data storage ('student_data.json')
- View all saved student records
- Interactive menu system 

---


## 🧠 Key Concepts & Skills Demonstrated

This project demonstrates understanding of:

- Dictionaries for structured data storage
- Loops and iteration
- Aggregation and calculations (averages)
- Use of max() and min() with key functions
- Input validation and user interaction
- File handling(text + JSON)
- Data persistence and simple storage systems
- JSON persistence
- Modular software design
  

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
5. File Handling/Persistence Layer
   - Saves results to a text file
   - Store structured data in JSON for reuse


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

## 📊 Data Analytics

A Python analytics module that loads students' data from a JSON file and generates a visual report using Matplotlib. This module is demonstrates data processing, modular programming, and data visualization.

# ⚙️ Features

- Load student data from a JSON file
- Extract student names and averages
- Generate a professional bar graph of student averages
- Display percentage labels above each bar
- Automatic graph scaling based on the highest mark to ensure readability
- Clear axis labels and gridlines for clarity

---

## 🛠️ Technologies Used

- Python 3
- Built-in data structures (dict, list)
- Conditional statements
- Functions for modular design
- Matplotlib
- JSON


---


## 📦 Dependencies

### Requirements
- Python 3.6 or higher
- Matplotlib

Install Matplotlib with:
```bash
pip install matplotlib
```

---


## 📁 Project Structure

sstudent-marks-system/
│
├── student_marks_system.py   # Main program logic
├── analytics.py              # Processes student records and generates bar graph
├── student_report.txt        # Generated reports
├── student_data.json         # Stored student records
├── README.md                 # Documentation
└── screenshots/
    ├── analytics.png
    ├── menu.png
    ├── json.png


---


## ▶️ How to Run the Project

Clone the repository:
git clone https://github.com/Sedi-dev/student-marks-system.git

Navigate into the project folder:
cd student-marks-system

Run the program:
python3 student_marks_system.py 


---


## 🚀 Recent Upgrades(May 2026)

### Version 2.0 - Menu System & JSON Persistence
This update transforms the project from a single-use script into a persistent multi-student system.

### 🔹 New Features
- **Interactive menu:** Add students, view all records,or exit
- **JSON data storage:** All records save to 'student_data.json' and load automatically
- **View all students:** Browse all saved records in a clean format
- **Persistent database:** Data survives between program runs
- **Data visualization:** Bar graph visualizing student averages

### 🔹 What this demonstrates
- File I/O with JSON
- Data persistence patterns
- User-centered menu design
- Professional application structure


---


## 💡 Learning Outcome

This project improved my ability to structure and analyze data using dictionaries, as well as apply built-in Python functions for efficient data processing. Through developing this project, I gained experience in:

- How to structure a program using multiple functions
- How to use dictionaries to model real-world data
- How to perform calculations on grouped data
- How to validate and sanitize user input
- How to design a clean output/report system
- Writing data to files and managing persistence
- Transition from simple scripts to structured systems
- Designing a bar graph to visualize student data


---


 ## 📌 Challenges Faced

One of the main challenges was designing a system that could handle multiple subjects dynamically while still producing accurate summaries. This was solved using dictionary-based storage and built-in Python functions like sum(), max(), and min().

A key challenge was designing a system that could handle multiple students while maintaining accurate calculations and clean data storage. This was solved by introducing structured dictionaries and extending the program with JSON-based persistence.

A recent challenge was learning the Matplotlib functions and designing a graph using them and the student records from a JSON file. 


---


## 🚀 Future Improvements

- Add GUI version (Tkinter or web-based interface)
- Export results as PDF report cards
- Add ranking system for multiple students
- SQLite database integration
- Grade distribution chart
- Pass/fail pie chart
- Subject comparison graphs
- Edit and delete student records


---


## 👨🏻‍💻 Program Demo

#Screenshots

### Adding a new student
![](https://github.com/user-attachments/assets/49710262-8536-4a96-aa8c-800c8f5b7195)



### Student number validation
![Invalid subject number](https://github.com/user-attachments/assets/bdc9830b-678f-4fde-9d66-f45654266330)



### Mark input validation
![Input validation for marks](https://github.com/user-attachments/assets/e0be98f3-46dc-4b28-a603-74d6741c12d4)



### Student Report
![student.txt](https://github.com/user-attachments/assets/57b7fd68-1d28-4ed5-8164-24e460e5c8b5)



### Saved Student Records
![Updated Student marks system running](https://github.com/user-attachments/assets/f0d62dbc-11a7-4636-85c1-9df911d678ce)



### Student Data JSON
![student_data.json example](https://github.com/user-attachments/assets/db163d69-d7fe-48cd-8910-0c1e3d4f2542)




### Analytics Dashboard
![analytics.py example run](https://github.com/user-attachments/assets/47dec57e-70ab-4364-ab10-4128338139ae)


---


## ⭐ Final Note

This project reflects my approach to learning:

Building complete, progressively improved applications to reinforce core programming concepts and develop practical problem-solving skills.


---

⭐ If you found this project interesting, feel free to explore my other repositories.

---

Last updated: May 2026

