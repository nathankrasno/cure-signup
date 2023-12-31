import sqlite3

# Create or connect to the database
conn = sqlite3.connect("databases/courses.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Course (
        courseID INTEGER PRIMARY KEY,
        courseCode TEXT,
        title TEXT,
        capacity INTEGER,
        description TEXT,
        meetingTime DATETIME,
        meetingLocation TEXT,
        professorID INTEGER,
        FOREIGN KEY (professorID) REFERENCES Professor(professorID)
    )
"""
)
conn.commit()
conn.close()

conn = sqlite3.connect("databases/professors.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Professor (
        professorID INTEGER PRIMARY KEY,
        first TEXT,
        last TEXT,
        email TEXT
    )
"""
)
conn.commit()
conn.close()

conn = sqlite3.connect("databases/students.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Student (
        ufid INTEGER PRIMARY KEY,
        first TEXT,
        last TEXT,
        email TEXT,
        choice1 INTEGER,
        choice2 INTEGER,
        choice3 INTEGER,
        assigned INTEGER,
        isRegistered BOOLEAN DEFAULT 0,
        isCompleted BOOLEAN DEFAULT 0,
        FOREIGN KEY (choice1) REFERENCES Course(courseID),
        FOREIGN KEY (choice2) REFERENCES Course(courseID),
        FOREIGN KEY (choice3) REFERENCES Course(courseID),
        FOREIGN KEY (assigned) REFERENCES Course(courseID)
    )
"""
)
# Commit changes and close the connection
conn.commit()
conn.close()
