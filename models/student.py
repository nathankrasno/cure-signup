import sqlite3


class Student:
    def __init__(
        self,
        ufid,
        first,
        last,
        email,
        choice1,
        choice2,
        choice3,
        assigned,
        isRegistered=False,
        isCompleted=False,
    ):
        self.ufid = ufid
        self.first = first
        self.last = last
        self.email = email
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.assigned = assigned
        self.isRegistered = isRegistered
        self.isCompleted = isCompleted
    def display(self):
        print(f"Student UFID: {self.ufid}")
        print(f"First Name: {self.first}")
        print(f"Last Name: {self.last}")
        print(f"Email: {self.email}")
        print(f"Choice 1: {self.choice1}")
        print(f"Choice 2: {self.choice2}")
        print(f"Choice 3: {self.choice3}")
        print(f"Assigned: {self.assigned}")
        print(f"Is Registered: {self.isRegistered}")
        print(f"Is Completed: {self.isCompleted}")
        print("-" * 20)
    def save(self):
        try:
            # Open a connection to the database
            conn = sqlite3.connect("databases/students.db")
            cursor = conn.cursor()

            # Insert student data into the Student table
            cursor.execute(
                """
                INSERT INTO Student (ufid, first, last, email, choice1, choice2, choice3, assigned, isRegistered, isCompleted)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    self.ufid,
                    self.first,
                    self.last,
                    self.email,
                    self.choice1,
                    self.choice2,
                    self.choice3,
                    self.assigned,
                    self.isRegistered,
                    self.isCompleted,
                ),
            )

            # Commit changes and close the connection
            conn.commit()
            conn.close()
            print("Student saved successfully.")
        except sqlite3.Error as e:
            print(f"Error saving student: {e}")

    def change_student_course(self, new_courseID):
        try:
            conn_stu = sqlite3.connect("databases/students.db")
            conn_course = sqlite3.connect("databases/courses.db")
            cursor_stu = conn_stu.cursor()

            # Check if the target course has available capacity
            cursor_stu.execute(
                """
                SELECT COUNT(*) FROM Student
                WHERE assigned = ? AND isRegistered = 1
                """,s
                (new_courseID,),
            )
            count = cursor_stu.fetchone()[0]
            cursor_course = conn_course.cursor()
            cursor_course.execute(
                """
                SELECT capacity FROM Course
                WHERE courseID = ?
                """,
                (new_courseID,),
            )
            capacity = cursor_course.fetchone()[0]
            if count >= capacity:
                print("The target course is already at full capacity. Course change not allowed.")
            else:
                # Update the student's assigned course ID
                cursor_stu.execute(
                    """
                    UPDATE Student
                    SET assigned = ?
                    WHERE ufid = ?
                    """,
                    (new_courseID, self.ufid),
                )
                conn_stu.commit()
                print(f"Student {self.ufid} has been reassigned to Course ID {new_courseID}.")

            conn_stu.close()
            conn_course.close()
        except sqlite3.Error as e:
            print(f"Error changing student's course: {e}")

