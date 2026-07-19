# 🎓 Student Management System

A menu-driven CRUD application built in pure Python to manage student records in memory. Supports adding, viewing, searching, updating, and deleting student data with clean formatted output and input validation.

---

## 📌 Overview

This project demonstrates core Python programming concepts — functions, lists, dictionaries, loops, and string methods — applied to build a real working application without any external libraries. It simulates a basic student database with full Create, Read, Update, and Delete (CRUD) operations through an interactive terminal menu.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ➕ Add Student | Add new student with ID, Name, Age, and Course with full validation |
| 📋 View Students | Display all records in a formatted table with sort options |
| 🔍 Search | Search by Student ID, Name (partial), or Course (partial) |
| ✏️ Update | Edit any field of an existing student — press Enter to keep current value |
| 🗑️ Delete | Remove a student with a confirmation prompt before deletion |
| 📊 Statistics | Total count, average age, youngest, oldest, and course-wise breakdown |

---

## 🛡️ Input Validations

- **Student ID** — must be a whole number and unique across all records
- **Name** — must contain only letters (spaces allowed), cannot be empty
- **Age** — must be a number between 5 and 100
- **Course** — cannot be empty
- **Duplicate name** — warns if same name already exists but allows it with confirmation
- **Delete** — requires explicit y/n confirmation before removing a record

---

## 📂 Project Structure

```
Student-management-system/
│
├── student_management.py    # Main application — all functions and menu
└── README.md
```

---

## ▶️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Killarilahari/Student-management-system-python.git
cd Student-management-system-python
```

**2. Run the script**
```bash
python student_management.py
```

> No external libraries required. Works with Python 3.6 and above.

---

## 🖥️ Sample Output

```
══════════════════════════════════════════════════════════════════
       🎓   STUDENT MANAGEMENT SYSTEM   🎓
══════════════════════════════════════════════════════════════════
    1️⃣   Add Student
    2️⃣   View All Students
    3️⃣   Search Student
    4️⃣   Update Student
    5️⃣   Delete Student
    6️⃣   Statistics
    7️⃣   Exit
──────────────────────────────────────────────────────────────────
  👉  Enter your choice (1-7):
```

**View Students (sorted by ID):**
```
══════════════════════════════════════════════════════════════════
  📘  STUDENT RECORDS  [Sorted by Name]
══════════════════════════════════════════════════════════════════
  No    ID       Name                 Age    Course
──────────────────────────────────────────────────────────────────
  1     101      vinni                21     Data Science
  2     102      Lahari               20     Computer Science
  3     103      Meghana              19     Electronics
──────────────────────────────────────────────────────────────────
  Total : 3 student(s)
```

**Statistics:**
```
  Total Students  : 3
  Average Age     : 20.0 years
  Youngest        : Meghana (Age 19)
  Oldest          : Vinni (Age 21)
──────────────────────────────────────────────────────────────────
  Course                    Students
──────────────────────────────────────────────────────────────────
  Computer Science          1  █
  Data Science              1  █
  Electronics               1  █
```

---

## 🔧 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
---

## 📚 Concepts Demonstrated

- Functions and modular code structure
- Lists and dictionaries for in-memory data storage
- String methods for input validation
- f-strings and formatted table output
- Lambda functions for sorting
- List comprehensions for searching
- CRUD operations without any database or framework

---

## 👩‍💻 Author

**Killari Lahari**

B.Tech – Computer Science and Engineering (AI and ML)

📧 laharikillari007@gmail.com

🔗 [LinkedIn](https://linkedin.com/in/lahari-killari-375587324)
