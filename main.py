import sqlite3
import pandas as pd
from models.student import Student
from models.professor import Professor
from models.course import Course

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
        print("6. Delete Student")
        print("7. Populate Courses & Professors")
        print("8. Display all courses")
        print("9. Display all professors")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            #create_course
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
            try:
                student = get_student_by_ufid(student_id)
                student.display()
            except Exception as e:
                print("invalid UFID, try again")
        elif choice == "6":
            #delete student
            delete_student()
            
        elif choice == "7":
            #read excel input
            print("Excel should have the following columns:")
            print("First,Last,Email,Course Title,Course Number,Course Cap,Description,Meeting Time,Meeting Location")
            print("Type the relative file location")
            file = input()
            professors_courses_from_excel(file)
            break
        elif choice == "8":
            #display courses
            display_all_courses()
            
        elif choice == "9":
            #display professors
            display_all_professors()
            
        elif choice == "10":
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
                s = Student(*student)
                s.display()
        else:
            print("No students found in the database.")

        # Close the connection
        conn.close()
    except sqlite3.Error as e:
        print(f"Error displaying students: {e}")

def display_all_courses():
    try:
        # Open a connection to the database
        conn = sqlite3.connect("databases/courses.db")
        cursor = conn.cursor()

        # Query and display all students
        cursor.execute("SELECT * FROM Course")
        courses = cursor.fetchall()

        if courses:
            print("Course Information:")
            for course in courses:
                c = Course(*course)
                print("="*10)
                c.display()
        else:
            print("No courses found in the database.")

        # Close the connection
        conn.close()
    except sqlite3.Error as e:
        print(f"Error displaying courses: {e}")

def display_all_professors():
    try:
        conn = sqlite3.connect("databases/professors.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT professorID, first, last
            FROM Professor
        """
        )

        results = cursor.fetchall()
        conn.close()

        if results:
            for professor in results:
                professorID, first, last = professor
                print(f"Professor ID: {professorID}, First Name: {first}, Last Name: {last}")
        else:
            print("No professors found.")

    except sqlite3.Error as e:
        print(f"Error retrieving professor info: {e}")

def get_student_by_ufid(ufid):
    try:
        # Open a connection to the database
        conn = sqlite3.connect("databases/students.db")
        cursor = conn.cursor()

        # Query the database to get student information by UFID
        cursor.execute("SELECT * FROM Student WHERE UFID = ?", (ufid,))
        student = cursor.fetchone()
        if student:
            s = Student(*student)
            return s
        else:
            print(f"No student found with UFID {ufid}.")
            return None

        # Close the connection
        conn.close()
    except sqlite3.Error as e:
        print(f"Error getting student information by UFID: {e}")
        return None

def create_student():
    print("UFID:")
    ufid = int(input())
    print("First Name:")
    first = input()
    print("Last Name:")
    last = input()
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
        ufid,
        first,
        last,
        email,
        choice1,
        choice2,
        choice3,
        assigned,
        isRegistered,
        isCompleted,
    )
    student.save()

def delete_student():
    print("="*20)
    print('Enter UFID')
    ufid = int(input())
    try:
        # Open a connection to the database
        conn = sqlite3.connect("databases/students.db")
        cursor = conn.cursor()

        # Query the database to get student information by UFID
        cursor.execute("SELECT * FROM Student WHERE UFID = ?", (ufid,))
        student = cursor.fetchone()
        s = Student(*student)
        print(f"Type '1' to confirm deleting {s.ufid}: {s.first} {s.last} with choices {s.choice1}, {s.choice2}, {s.choice3}")
        confirm = input()
        if confirm == "1":
            cursor.execute("DELETE FROM Student WHERE UFID = ?", (ufid,))
            conn.commit()
            conn.close()
        else:
            print("Canceling...")
            conn.close()
            return
    except sqlite3.Error as e:
        print(f"Error getting student information by UFID: {e}")
        return None

def professors_courses_from_excel(file):
    try:
        # Read data from the Excel file
        df = pd.read_excel(file)

        print(df.head())

        for index, row in df.iterrows():
            professor = Professor(row['First'], row['Last'], row['Email'])
            professor.save()
            professorID = professor.get_id()
            course = Course(
                row['Course Title'],
                row['Course Number'],
                row['Course Cap'],
                row['Description'],
                row['Meeting Time'],
                row['Meeting Location'],
                professorID,
            )
            course.save()

        print("Data import successful.")
    except Exception as e:
        print(f"Error importing data: {e}")
if __name__ == "__main__":
    main()
