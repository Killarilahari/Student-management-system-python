students = []

def add_student():
    print("\n🟢 ADD NEW STUDENT")

    sid = input("Student ID   : ")

    # 🔒 UNIQUE ID CHECK LOGIC
    for s in students:
        if s["id"] == sid:
            print("❌ Student ID already exists! Please enter a unique ID.")
            return

    name = input("Student Name : ")

    if name.strip() == "":
        print("❌ Name cannot be empty!")
        return

    age = input("Student Age  : ")
    course = input("Course       : ")

    students.append({
        "id": sid,
        "name": name,
        "age": age,
        "course": course
    })

    print("✅ Student added successfully!")


def view_students():
    if not students:
        print("\n⚠️ No student records available.")
        return

    print("\n📘 STUDENT RECORDS")
    print("-" * 55)
    print(f"{'No':<5}{'ID':<10}{'Name':<18}{'Age':<6}{'Course'}")
    print("-" * 55)

    for i, s in enumerate(students, start=1):
        print(f"{i:<5}{s['id']:<10}{s['name']:<18}{s['age']:<6}{s['course']}")

    print("-" * 55)


def update_student():
    print("\n✏️ UPDATE STUDENT")
    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:
            s["name"] = input("New Name   : ")
            s["age"] = input("New Age    : ")
            s["course"] = input("New Course : ")
            print("✅ Student updated successfully!")
            return

    print("❌ Student ID not found.")


def delete_student():
    print("\n🗑️ DELETE STUDENT")
    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("✅ Student deleted successfully!")
            return

    print("❌ Student ID not found.")


# MAIN MENU
while True:
    print("\n" + "=" * 40)
    print("🎓  STUDENT MANAGEMENT SYSTEM  🎓")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("👉 Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("\n👋 Program exited successfully.")
        break
    else:
        print("❌Student ID already exists! Please enter a unique ID.")