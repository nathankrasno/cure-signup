import sqlite3

class Professor:
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email
    def display(self):
        print(f"Professor First Name: {self.first}")
        print(f"Professor Last Name: {self.last}")
        print(f"Professor Email: {self.email}")
        print("-" * 20)
    def save(self):
        try:
            conn = sqlite3.connect("databases/professors.db")
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO Professor (first, last, email)
                VALUES (?, ?, ?)
            """,
                (self.first, self.last, self.email),
            )

            conn.commit()
            conn.close()
            print("Professor saved successfully.")
        except sqlite3.Error as e:
            print(f"Error saving professor: {e}")
            
    def get_id(self):
        try:
            conn = sqlite3.connect("databases/professors.db")
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT professorID FROM Professor
                WHERE first = ? AND last = ?
                """,
                (self.first, self.last)
            )

            result = cursor.fetchone()  # Fetch the result
            conn.close()

            if result:
                return result[0]  # Return the professorID
            else:
                return None  # Professor not found

        except sqlite3.Error as e:
            print(f"Error retrieving professor ID: {e}")
            return None
