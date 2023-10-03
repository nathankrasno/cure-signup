import sqlite3


class Student:
    def __init__(
        self,
        first,
        last,
        ufid,
        email,
        choice1,
        choice2,
        choice3,
        assigned,
        isRegistered=False,
        isCompleted=False,
    ):
        self.first = first
        self.last = last
        self.ufid = ufid
        self.email = email
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.assigned = assigned
        self.isRegistered = isRegistered
        self.isCompleted = isCompleted

    def save(self):
        try:
            # Open a connection to the database
            conn = sqlite3.connect("databases/students.db")
            cursor = conn.cursor()

            # Insert student data into the Student table
            cursor.execute(
                """
                INSERT INTO Student (first, last, ufid, email, choice1, choice2, choice3, assigned, isRegistered, isCompleted)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    self.first,
                    self.last,
                    self.ufid,
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
