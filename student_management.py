students = []


def add_student():
    print("\n🟢 ADD NEW STUDENT")

    # 🔹 ID must be integer & unique
    sid = input("Student ID   : ")
    if not sid.isdigit():
        print("❌ Student ID must be an integer!")
        return

    sid = int(sid)

    for s in students:
        if s["id"] == sid:
            print("❌ Student ID already exists! Please enter a unique ID.")
            return

    # 🔹 Name must be non-empty and alphabets
    name = input("Student Name : ").strip()
    if not name.isalpha():
        print("❌ Name must a string!")
        return

    # 🔹 Age must be integer
    age = input("Student Age  : ")
    if not age.isdigit():
        print("❌ Age must be a number!")
        return

    age = int(age)

    # 🔹 Course must not be empty
    course = input("Course       : ").strip()
    if course == "":
        print("❌ Course cannot be empty!")
        return

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

    if not sid.isdigit():
        print("❌ Student ID must be an integer!")
        return

    sid = int(sid)

    for s in students:
        if s["id"] == sid:
            name = input("New Name   : ").strip()
            if name.isalpha():
                s["name"] = name

            age = input("New Age    : ")
            if age.isdigit():
                s["age"] = int(age)

            course = input("New Course : ").strip()
            if course != "":
                s["course"] = course

            print("✅ Student updated successfully!")
            return

    print("❌ Student ID not found.")


def delete_student():
    print("\n🗑️ DELETE STUDENT")
    sid = input("Enter Student ID: ")

    if not sid.isdigit():
        print("❌ Student ID must be an integer!")
        return

    sid = int(sid)

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("✅ Student deleted successfully!")
            return

    print("❌ Student ID not found.")


# 🔹 MAIN MENU
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
        print("❌ Invalid choice! Please enter between 1 and 5.")
