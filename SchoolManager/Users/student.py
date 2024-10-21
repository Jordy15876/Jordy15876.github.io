from database import connect_db
from Users.user import User


class Student(User):
    def view_profile(self):
        """Display the student's profile, including personal information and marks.

        This method retrieves the student's details from the database using their username 
        (which is their student ID). It also fetches the marks for each subject the student is enrolled in.
        """
        conn = connect_db()  # Establish a connection to the database
        cursor = conn.cursor()
        
        # Fetch the student's personal information
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (self.username,))
        student = cursor.fetchone()
        
        # Fetch the marks associated with the student's ID
        cursor.execute("SELECT subject, marks FROM scores WHERE student_id = ?", (self.username,))
        marks = cursor.fetchall()
        conn.close()  # Close the database connection after retrieving data

        if student:
            # Display the student's profile information
            print(f"\n--- Student Profile ---")
            print(f"ID: {student[0]}")         # Student ID
            print(f"Name: {student[1]}")       # Student Name
            print(f"Grade: {student[2]}")      # Student Grade
            print(f"Address: {student[3]}")    # Student Address
            
            print(f"--- Marks ---")  # Header for marks section
            if marks:
                # If marks are found, display them
                for subject, mark in marks:
                    print(f"Subject: {subject}, Marks: {mark}")
            else:
                # If no marks are found, inform the user
                print("No marks found for this student.")
        else:
            # If no student record is found, notify the user
            print("Student record not found.")

    def view_marks(self):
        """Display the marks for subjects the student is enrolled in.

        This method retrieves the marks associated with the student's ID from the database and displays them.
        If no marks are found, it informs the user accordingly.
        """
        conn = connect_db()  # Establish a connection to the database
        cursor = conn.cursor()
        
        # Fetch the marks for the student based on their ID
        cursor.execute("SELECT subject, marks FROM scores WHERE student_id = ?", (self.username,))
        marks = cursor.fetchall()
        conn.close()  # Close the database connection after retrieving data

        if marks:
            # If marks are found, display them
            print(f"\n--- Marks for {self.username} ---")  # Header for marks section
            for subject, mark in marks:
                print(f"Subject: {subject}, Marks: {mark}")
        else:
            # If no marks are found, notify the user
            print("No marks found for this student.")
