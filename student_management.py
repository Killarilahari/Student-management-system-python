import os

# DATA STORE

students = []

# HELPERS

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def divider(char="─", width=65):
    print(char * width)

def header(title):
    print()
    divider("═")
    print(f"  {title}")
    divider("═")

def get_int_input(prompt):
    """Returns integer or None if invalid."""
    val = input(prompt).strip()
    if val.isdigit():
        return int(val)
    print("  ❌  Must be a whole number.")
    return None

def get_text_input(prompt, allow_spaces=False):
    """Returns stripped text or None if empty/invalid."""
    val = input(prompt).strip()
    if val == "":
        print("  ❌  This field cannot be empty.")
        return None
    if not allow_spaces and not val.replace(" ", "").isalpha():
        print("  ❌  Only letters allowed.")
        return None
    return val

def find_student(sid):
    for s in students:
        if s["id"] == sid:
            return s
    return None

def print_table(data, title="STUDENT RECORDS"):
    if not data:
        print("\n  ⚠️  No records to display.")
        return
    header(f"📘  {title}")
    print(f"  {'No':<5} {'ID':<8} {'Name':<20} {'Age':<6} {'Course':<20}")
    divider()
    for i, s in enumerate(data, 1):
        print(f"  {i:<5} {s['id']:<8} {s['name']:<20} {s['age']:<6} {s['course']:<20}")
    divider()
    print(f"  Total : {len(data)} student(s)")

# ─────────────────────────────────────────────────────────────────────────────
# 1. ADD STUDENT
# ─────────────────────────────────────────────────────────────────────────────
def add_student():
    header("🟢  ADD NEW STUDENT")

    # ID
    sid = get_int_input("  Student ID   : ")
    if sid is None:
        return
    if find_student(sid):
        print(f"  ❌  ID {sid} already exists. Please use a unique ID.")
        return

    # Name
    name = get_text_input("  Student Name : ", allow_spaces=True)
    if name is None:
        return
    # Warn if same name already exists (but allow it)
    same_name = [s for s in students if s["name"].lower() == name.lower()]
    if same_name:
        print(f"  ⚠️  Warning: A student named '{name}' already exists (ID: {same_name[0]['id']}).")
        confirm = input("  Continue anyway? (y/n): ").strip().lower()
        if confirm != "y":
            print("  ↩️  Cancelled.")
            return

    # Age
    age = get_int_input("  Student Age  : ")
    if age is None:
        return
    if not (5 <= age <= 100):
        print("  ❌  Age must be between 5 and 100.")
        return

    # Course
    course = get_text_input("  Course       : ", allow_spaces=True)
    if course is None:
        return

    students.append({"id": sid, "name": name, "age": age, "course": course})
    print(f"\n  ✅  Student '{name}' added successfully!")

# ─────────────────────────────────────────────────────────────────────────────
# 2. VIEW ALL STUDENTS
# ─────────────────────────────────────────────────────────────────────────────
def view_students():
    if not students:
        print("\n  ⚠️  No student records available.")
        return

    print("\n  Sort by: (1) ID  (2) Name  (3) Age  (4) Course  (5) No sort")
    choice = input("  Choose sort option: ").strip()

    sort_map = {
        "1": ("id",     "Sorted by ID"),
        "2": ("name",   "Sorted by Name"),
        "3": ("age",    "Sorted by Age"),
        "4": ("course", "Sorted by Course"),
    }
    if choice in sort_map:
        key, label = sort_map[choice]
        data = sorted(students, key=lambda s: s[key])
        print_table(data, f"STUDENT RECORDS  [{label}]")
    else:
        print_table(students)

# ─────────────────────────────────────────────────────────────────────────────
# 3. SEARCH STUDENT
# ─────────────────────────────────────────────────────────────────────────────
def search_student():
    header("🔍  SEARCH STUDENT")
    print("  Search by: (1) Student ID  (2) Name  (3) Course")
    choice = input("  Choose option: ").strip()

    if choice == "1":
        sid = get_int_input("  Enter Student ID: ")
        if sid is None:
            return
        s = find_student(sid)
        result = [s] if s else []

    elif choice == "2":
        name = input("  Enter Name (or part of it): ").strip().lower()
        result = [s for s in students if name in s["name"].lower()]

    elif choice == "3":
        course = input("  Enter Course (or part of it): ").strip().lower()
        result = [s for s in students if course in s["course"].lower()]

    else:
        print("  ❌  Invalid option.")
        return

    if result:
        print_table(result, f"SEARCH RESULTS  ({len(result)} found)")
    else:
        print("\n  ⚠️  No matching records found.")

# ─────────────────────────────────────────────────────────────────────────────
# 4. UPDATE STUDENT
# ─────────────────────────────────────────────────────────────────────────────
def update_student():
    header("✏️  UPDATE STUDENT")

    sid = get_int_input("  Enter Student ID to update: ")
    if sid is None:
        return

    s = find_student(sid)
    if not s:
        print(f"  ❌  No student found with ID {sid}.")
        return

    print(f"\n  Current record → ID: {s['id']}  |  Name: {s['name']}  |  Age: {s['age']}  |  Course: {s['course']}")
    print("  Press ENTER to keep current value.\n")

    # Name
    new_name = input(f"  New Name   [{s['name']}]: ").strip()
    if new_name:
        if new_name.replace(" ", "").isalpha():
            s["name"] = new_name
        else:
            print("  ⚠️  Invalid name — keeping current value.")

    # Age
    new_age = input(f"  New Age    [{s['age']}]: ").strip()
    if new_age:
        if new_age.isdigit() and 5 <= int(new_age) <= 100:
            s["age"] = int(new_age)
        else:
            print("  ⚠️  Invalid age — keeping current value.")

    # Course
    new_course = input(f"  New Course [{s['course']}]: ").strip()
    if new_course:
        s["course"] = new_course

    print(f"\n  ✅  Student ID {sid} updated successfully!")

# ─────────────────────────────────────────────────────────────────────────────
# 5. DELETE STUDENT
# ─────────────────────────────────────────────────────────────────────────────
def delete_student():
    header("🗑️  DELETE STUDENT")

    sid = get_int_input("  Enter Student ID to delete: ")
    if sid is None:
        return

    s = find_student(sid)
    if not s:
        print(f"  ❌  No student found with ID {sid}.")
        return

    print(f"\n  Record to delete → ID: {s['id']}  |  Name: {s['name']}  |  Course: {s['course']}")
    confirm = input("  Are you sure? This cannot be undone. (y/n): ").strip().lower()

    if confirm == "y":
        students.remove(s)
        print(f"  ✅  Student '{s['name']}' deleted successfully!")
    else:
        print("  ↩️  Deletion cancelled.")

# ─────────────────────────────────────────────────────────────────────────────
# 6. STATISTICS
# ─────────────────────────────────────────────────────────────────────────────
def show_statistics():
    if not students:
        print("\n  ⚠️  No student records available.")
        return

    header("📊  STATISTICS")

    total = len(students)
    avg_age = sum(s["age"] for s in students) / total
    youngest = min(students, key=lambda s: s["age"])
    oldest   = max(students, key=lambda s: s["age"])

    # Course-wise count
    course_count = {}
    for s in students:
        c = s["course"]
        course_count[c] = course_count.get(c, 0) + 1

    print(f"  Total Students  : {total}")
    print(f"  Average Age     : {avg_age:.1f} years")
    print(f"  Youngest        : {youngest['name']} (Age {youngest['age']})")
    print(f"  Oldest          : {oldest['name']} (Age {oldest['age']})")
    divider()
    print(f"  {'Course':<25} {'Students'}")
    divider()
    for course, count in sorted(course_count.items()):
        bar = "█" * count
        print(f"  {course:<25} {count}  {bar}")
    divider()

# ─────────────────────────────────────────────────────────────────────────────
# MAIN MENU
# ─────────────────────────────────────────────────────────────────────────────
def main():
    while True:
        print("\n")
        divider("═")
        print("       🎓   STUDENT MANAGEMENT SYSTEM   🎓")
        divider("═")
        print("    1️⃣   Add Student")
        print("    2️⃣   View All Students")
        print("    3️⃣   Search Student")
        print("    4️⃣   Update Student")
        print("    5️⃣   Delete Student")
        print("    6️⃣   Statistics")
        print("    7️⃣   Exit")
        divider()

        choice = input("  👉  Enter your choice (1-7): ").strip()

        if   choice == "1": add_student()
        elif choice == "2": view_students()
        elif choice == "3": search_student()
        elif choice == "4": update_student()
        elif choice == "5": delete_student()
        elif choice == "6": show_statistics()
        elif choice == "7":
            print("\n  👋  Thank you for using Student Management System.\n")
            break
        else:
            print("  ❌  Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
