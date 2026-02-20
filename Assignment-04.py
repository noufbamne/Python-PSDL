'''# Student Management System using Dictionary

students = {}

def add_student():
    sid = input("Enter Student ID: ").strip()
    if not sid:
        print("ID cannot be empty.")
        return
    if sid in students:
        print("Student ID already exists!")
        return

    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter Age: "))
        if age <= 0:
            print("Invalid age.")
            return
    except:
        print("Age must be a number.")
        return

    student_class = input("Enter Class: ").strip()
    if not student_class:
        print("Class cannot be empty.")
        return

    try:
        marks = float(input("Enter Marks (0-100): "))
        if not (0 <= marks <= 100):
            print("Marks must be between 0 and 100.")
            return
    except:
        print("Marks must be a number.")
        return

    students[sid] = {
        "Name": name,
        "Age": age,
        "Class": student_class,
        "Marks": marks
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    for sid, d in students.items():
        print(f"\nStudent ID: {sid}")
        for k, v in d.items():
            print(f"{k}: {v}")


def search_student():
    sid = input("Enter Student ID: ")
    d = students.get(sid)

    if not d:
        print("Student not found.")
        return

    for k, v in d.items():
        print(f"{k}: {v}")


def update_student():
    sid = input("Enter Student ID: ")
    if sid not in students:
        print("Student not found.")
        return

    d = students[sid]

    name = input(f"Name [{d['Name']}]: ")
    if name:
        d["Name"] = name

    age = input(f"Age [{d['Age']}]: ")
    if age:
        try:
            d["Age"] = int(age)
        except:
            print("Invalid age — kept old value.")

    student_class = input(f"Class [{d['Class']}]: ")
    if student_class:
        d["Class"] = student_class

    marks = input(f"Marks [{d['Marks']}]: ")
    if marks:
        try:
            m = float(marks)
            if 0 <= m <= 100:
                d["Marks"] = m
        except:
            print("Invalid marks — kept old value.")

    print("Student updated.")


def delete_student():
    sid = input("Enter Student ID: ")
    if sid not in students:
        print("Student not found.")
        return

    confirm = input("Delete? (y/n): ").lower()
    if confirm == "y":
        del students[sid]
        print("Deleted.")
    else:
        print("Cancelled.")


def students_above_marks():
    try:
        limit = float(input("Enter minimum marks: "))
    except:
        print("Invalid number.")
        return

    found = False
    for sid, d in students.items():
        if d["Marks"] > limit:
            print(f"{sid} - {d['Name']} ({d['Marks']})")
            found = True

    if not found:
        print("No students above that mark.")


def highest_marks():
    if not students:
        print("No records.")
        return

    sid, d = max(students.items(), key=lambda x: x[1]["Marks"])
    print("\nTop Student:")
    print("ID:", sid)
    for k, v in d.items():
        print(f"{k}: {v}")


# -------- Menu --------

while True:
    print("\n--- Student Management System ---")
    print("1 Add")
    print("2 View")
    print("3 Search")
    print("4 Update")
    print("5 Delete")
    print("6 Above Marks")
    print("7 Highest Marks")
    print("8 Exit")

    ch = input("Choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        search_student()
    elif ch == "4":
        update_student()
    elif ch == "5":
        delete_student()
    elif ch == "6":
        students_above_marks()
    elif ch == "7":
        highest_marks()
    elif ch == "8":
        break
    else:
        print("Invalid choice.")
'''

# Student Management System using Dictionary

students = {}

def add_student():
    sid = input("Enter Student ID: ")
    if sid == "":
        print("ID cannot be empty")
        return
    if sid in students:
        print("Student ID already exists")
        return

    name = input("Enter Name: ")
    if name == "":
        print("Name cannot be empty")
        return

    age = input("Enter Age: ")
    if not age.isdigit():
        print("Age must be number")
        return
    age = int(age)

    student_class = input("Enter Class: ")
    if student_class == "":
        print("Class cannot be empty")
        return

    marks = input("Enter Marks (0-100): ")
    if not marks.replace(".", "").isdigit():
        print("Marks must be number")
        return
    marks = float(marks)

    if marks < 0 or marks > 100:
        print("Marks out of range")
        return

    students[sid] = {
        "Name": name,
        "Age": age,
        "Class": student_class,
        "Marks": marks
    }

    print("Student added successfully")


def view_students():
    if students == {}:
        print("No records found")
        return

    for sid in students:
        print("\nStudent ID:", sid)
        details = students[sid]
        for key in details:
            print(key, ":", details[key])


def search_student():
    sid = input("Enter Student ID: ")
    if sid not in students:
        print("Student not found")
        return

    details = students[sid]
    for key in details:
        print(key, ":", details[key])


def update_student():
    sid = input("Enter Student ID: ")
    if sid not in students:
        print("Student not found")
        return

    details = students[sid]

    name = input("Enter new name (leave blank to keep same): ")
    if name != "":
        details["Name"] = name

    age = input("Enter new age: ")
    if age.isdigit():
        details["Age"] = int(age)

    student_class = input("Enter new class: ")
    if student_class != "":
        details["Class"] = student_class

    marks = input("Enter new marks: ")
    if marks.replace(".", "").isdigit():
        m = float(marks)
        if m >= 0 and m <= 100:
            details["Marks"] = m

    print("Student updated")


def delete_student():
    sid = input("Enter Student ID: ")
    if sid not in students:
        print("Student not found")
        return

    confirm = input("Confirm delete (y/n): ")
    if confirm == "y":
        del students[sid]
        print("Record deleted")
    else:
        print("Cancelled")


def students_above_marks():
    limit = input("Enter minimum marks: ")
    if not limit.replace(".", "").isdigit():
        print("Invalid number")
        return

    limit = float(limit)
    found = False

    for sid in students:
        if students[sid]["Marks"] > limit:
            print(sid, "-", students[sid]["Name"], students[sid]["Marks"])
            found = True

    if found == False:
        print("No students above given marks")


def highest_marks():
    if students == {}:
        print("No records")
        return

    top_id = ""
    top_marks = -1

    for sid in students:
        if students[sid]["Marks"] > top_marks:
            top_marks = students[sid]["Marks"]
            top_id = sid

    print("\nHighest Marks Student:")
    print("ID:", top_id)
    for key in students[top_id]:
        print(key, ":", students[top_id][key])


# -------- Menu --------

while True:
    print("\n--- Student Management System ---")
    print("1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Update Student")
    print("5 Delete Student")
    print("6 Students Above Marks")
    print("7 Highest Marks")
    print("8 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        students_above_marks()
    elif choice == "7":
        highest_marks()
    elif choice == "8":
        break
    else:
        print("Invalid choice")
