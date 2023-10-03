import sqlite3
from models.student import Student

# from models.professor import Professor
# from models.course import Course


def main():
    # Initialize the database (you can define this function in database.py)
    # Load initial data from CSV files (if needed)

    while True:
        # Display menu options to the user
        print("1. Create Course")
        print("2. Create Professor")
        print("3. Create Student")
        print("4. Move Student to New Class")
        print("5. Print Student Info")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Create a new course
            # Course.create_course()
            break

        elif choice == "2":
            # Create a new professor
            # Professor.create_professor()
            break

        elif choice == "3":
            # Create a new student
            # Input prompts for each attribute
            create_student()

        elif choice == "4":
            # Move a student to a new class
            # Student.move_student()
            break

        elif choice == "5":
            # Print student info
            print("Enter Student UFID: ")
            student_id = input()
            student_info = get_student_by_ufid(student_id)
            print("=" * 20)
            for key, value in student_info.items():
                print(f"{key}: {value}")
            print("=" * 20)

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


def display():
    try:
        # Open a connection to the database
        conn = sqlite3.connect("databases/students.db")
        cursor = conn.cursor()

        # Query and display all students
        cursor.execute("SELECT * FROM Student")
        students = cursor.fetchall()

        if students:
            print("Student Information:")
            for student in students:
                print(f"First Name: {student[0]}")
                print(f"Last Name: {student[1]}")
                print(f"Student ID: {student[2]}")
                print(f"Email: {student[3]}")
                print(f"Choice 1: {student[4]}")
                print(f"Choice 2: {student[5]}")
                print(f"Choice 3: {student[6]}")
                print(f"Assigned: {student[7]}")
                print(f"Is Registered: {student[8]}")
                print(f"Is Completed: {student[9]}")
                print("-" * 20)
        else:
            print("No students found in the database.")

        # Close the connection
        conn.close()
    except sqlite3.Error as e:
        print(f"Error displaying students: {e}")


def get_student_by_ufid(ufid):
    try:
        # Open a connection to the database
        conn = sqlite3.connect("databases/students.db")
        cursor = conn.cursor()

        # Query the database to get student information by UFID
        cursor.execute("SELECT * FROM Student WHERE UFID = ?", (ufid,))
        student = cursor.fetchone()

        if student:
            student_info = {
                "First Name": student[0],
                "Last Name": student[1],
                "UFID": student[2],
                "Email": student[3],
                "Choice 1": student[4],
                "Choice 2": student[5],
                "Choice 3": student[6],
                "Assigned": student[7],
                "Is Registered": student[8],
                "Is Completed": student[9],
            }
            return student_info
        else:
            print(f"No student found with UFID {ufid}.")
            return None

        # Close the connection
        conn.close()
    except sqlite3.Error as e:
        print(f"Error getting student information by UFID: {e}")
        return None


def create_student():
    print("First Name:")
    first = input()
    print("Last Name:")
    last = input()
    print("UFID:")
    ufid = int(input())
    print("Email:")
    email = input()
    print("Choice 1 (Course ID):")
    choice1 = input()
    print("Choice 2 (Course ID):")
    choice2 = input()
    print("Choice 3 (Course ID):")
    choice3 = input()
    print("Assigned (Course ID):")
    assigned = input()
    print("Is Registered (True/False):")
    isRegistered = input().lower() == "true"
    print("Is Completed (True/False):")
    isCompleted = input().lower() == "true"
    student = Student(
        first,
        last,
        ufid,
        email,
        choice1,
        choice2,
        choice3,
        assigned,
        isRegistered,
        isCompleted,
    )
    student.save()


if __name__ == "__main__":
    main()
