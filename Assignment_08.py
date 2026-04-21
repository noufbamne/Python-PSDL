import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nouf@0125",   # use your password
    database="student_db"
)
print("Connected successfully!")

cursor = conn.cursor()

# 1. Insert
def insert_data():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)",
        (name, age, course)
    )
    conn.commit()
    print("Inserted successfully")

# 2. Update
def update_data():
    id = int(input("Enter ID: "))
    name = input("Enter new name: ")

    cursor.execute(
        "UPDATE students SET name=%s WHERE id=%s",
        (name, id)
    )
    conn.commit()
    print("Updated successfully")

# 3. Delete
def delete_data():
    id = int(input("Enter ID: "))

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (id,)
    )
    conn.commit()
    print("Deleted successfully")

# 4. Search
def search_data():
    id = int(input("Enter ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id=%s",
        (id,)
    )
    result = cursor.fetchone()

    if result:
        print("Found:", result)
    else:
        print("Not found")

# 5. Display
def display_data():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

# Menu
while True:
    print("\n1.Insert 2.Update 3.Delete 4.Search 5.Display 6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        insert_data()
    elif ch == 2:
        update_data()
    elif ch == 3:
        delete_data()
    elif ch == 4:
        search_data()
    elif ch == 5:
        display_data()
    elif ch == 6:
        break
    else:
        print("Invalid choice")