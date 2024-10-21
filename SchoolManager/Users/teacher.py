from database import connect_db
from Users.user import User

class Teacher(User):
    def __init__(self, username, password, subject_name, teaching_grade): # This will configure the information for the teacher
        super().__init__(username, password) # This will call the User class to be the one that handles the login credentials
        self.subject_name = subject_name # This will store the subject that the teacher is teaching
        self.teaching_grade = teaching_grade # This will store the grade level that the teacher is teaching

    def view_student_records(self):
        """View all students in the teacher's teaching grade."""
        conn = connect_db() # This establishes the connection to the database
        cursor = conn.cursor() # Creates a cursor object which will allow for the execution of SQL quries
        # Beloe is a SQL query that will select all students from the database who are in the teacher's grade
        cursor.execute("SELECT * FROM students WHERE grade = ?", (self.teaching_grade,))
        students = cursor.fetchall() # This will obtain all the results from the executed query
        conn.close() # This closes the connection to the database. This allows for resources to be free'd up
        # Print the list of students for the teacher's reference.
        print(f"\n--- Students in Grade {self.teaching_grade} ---")
        for student in students:
            # Each student record contains an ID, name, grade, and address. Print them in a readable format.
            print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}, Address: {student[3]}")

    def add_marks(self, student_id, marks):
        """Add marks for a student in the subject taught by this teacher."""
        conn = connect_db()  # Connect to the database.
        cursor = conn.cursor()  # Create a cursor for executing SQL commands.

        # Retrieve the student's name using their ID. This is for logging purposes and to provide feedback.
        cursor.execute("SELECT name FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()  # Fetch the student's details based on the provided ID.
        
        if student:  # Check if the student was found.
            student_name = student[0]  # Extract the student's name from the fetched record.
            
            # This will insert the student's marks into the scores table for the subject they are being graded in.
            cursor.execute("INSERT INTO scores (student_id, subject, marks) VALUES (?, ?, ?)",
                           (student_id, self.subject_name, marks))
            conn.commit()  
            
            # Inform the teacher that the marks have been added successfully, including the student's name for clarity.
            print(f"Marks added for {student_name} (ID: {student_id}) in {self.subject_name}.")
        else:
            # This will notify the teacher that no corresponding student has been found to match the ID
            print(f"No student found with ID {student_id}.")

        conn.close()  # Close the database connection.

    def edit_marks(self, student_id, marks):
        """Update the marks for a student in the subject taught by this teacher."""
        conn = connect_db()  
        cursor = conn.cursor()  

        # SQL command to update the marks for a specific student in the scores table.
        cursor.execute("UPDATE scores SET marks = ? WHERE student_id = ? AND subject = ?",
                       (marks, student_id, self.subject_name))
        conn.commit()  # This allow for the changes to be committed to the database
        conn.close()  # Close the connection.
        
        # Inform the teacher that the marks have been updated successfully.
        print(f"Marks updated for student ID {student_id} in {self.subject_name}.")

    def view_subject(self):
        """Show the subject the teacher is responsible for."""
        # This will print out the subject being taught by the teacher for their own reference.
        print(f"{self.username} teaches: {self.subject_name}")

    def view_marks(self):
        """Retrieve and display all marks for students in this teacher's subject."""
        conn = connect_db()  # Connect to the database.
        cursor = conn.cursor()  # Create a cursor to execute SQL commands.
        
        # The below is a SQL query that joins students and scores to get a complete view of student marks for the subject.
        cursor.execute("""
            SELECT s.id, s.name, sc.marks 
            FROM students s 
            JOIN scores sc ON s.id = sc.student_id 
            WHERE sc.subject = ?
        """, (self.subject_name,))
        
        marks = cursor.fetchall()  
        conn.close()  

        # The below will print the marks for each student in a readable format.
        print(f"\n--- Marks for {self.subject_name} ---")
        if marks:
            for student_id, student_name, mark in marks:
                # Display each student's ID, name, and their corresponding marks.
                print(f"Student ID: {student_id}, Name: {student_name}, Marks: {mark}")
        else:
            # If no marks are found, this will let the teacher know.
            print("No marks found for this subject.")