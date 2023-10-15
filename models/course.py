import sqlite3

class Course:
    def __init__(self, courseID, courseCode, title, capacity, description, meetingTime, meetingLocation, professorID):
        self.courseID = courseID
        self.courseCode = courseCode
        self.title = title
        self.capacity = capacity
        self.description = description
        self.meetingTime = meetingTime
        self.meetingLocation = meetingLocation
        self.professorID = professorID

    def display(self):
        print(f"Course ID: {self.courseID}")
        print(f"Course Code: {self.courseCode}")
        print(f"Course Title: {self.title}")
        print(f"Capacity: {self.capacity}")
        print(f"Description: {self.description}")
        print(f"Meeting Time: {self.meetingTime}")
        print(f"Meeting Location: {self.meetingLocation}")
        print(f"Professor ID: {self.professorID}")
        print("-" * 20)

    def save(self):
        try:
            conn = sqlite3.connect("databases/courses.db")
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO Course (courseCode, title, capacity, description, meetingTime, meetingLocation, professorID)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (self.courseCode, self.title, self.capacity, self.description, self.meetingTime, self.meetingLocation, self.professorID),
            )

            conn.commit()
            conn.close()
            print("Course saved successfully.")
        except sqlite3.Error as e:
            print(f"Error saving course: {e}")
