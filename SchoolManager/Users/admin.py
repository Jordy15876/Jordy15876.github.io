from database import connect_db  # This will import the function to connect to the database.
from Users.user import User  # This will import the base User class to inherit user functionalities.

class Admin(User):
    def add_student(self, student_id, student_name, student_grade, address):
        """Add a new student to the database.

        Args:
            student_id (str): Unique identifier for the student.
            student_name (str): Name of the student.
            student_grade (int): Grade level of the student.
            address (str): Home address of the student.
        """
        conn = connect_db()  # This establishes connection to the database
        cursor = conn.cursor()  # This creates a cursor object which will execute SQL queries

        # Insert the new student's information into the students table.
        cursor.execute("INSERT INTO students (student_id, name, grade, address) VALUES (?, ?, ?, ?)", 
                       (student_id, student_name, student_grade, address))
        
        conn.commit()  # This commits the changes to save the new student in the database.
        conn.close()  # This closes the database to free up the resources

        # This informs the admin that the Student name has been addedd successfully
        print(f"Student {student_name} added successfully.")

    def edit_student(self, student_id, **kwargs): #  Update student information based on provided attributes. kwargs: Arbitrary keyword arguments that denote the fields to be updated (representing name, grade, and address).

        conn = connect_db()  
        cursor = conn.cursor()  

        
        if 'name' in kwargs:
            cursor.execute("UPDATE students SET name = ? WHERE student_id = ?", (kwargs['name'], student_id))
        
        # Update the student's grade if provided in kwargs.
        if 'grade' in kwargs:
            cursor.execute("UPDATE students SET grade = ? WHERE student_id = ?", (kwargs['grade'], student_id))
        
        # Update the student's address if provided in kwargs.
        if 'address' in kwargs:
            cursor.execute("UPDATE students SET address = ? WHERE student_id = ?", (kwargs['address'], student_id))

        conn.commit()  # Commit the changes to save the updates in the database.
        conn.close()  # Close the connection.

        # Inform the admin that the student's information has been updated.
        print("Student information updated.")

    def view_students(self):
        """Display a list of all students in the database."""
        conn = connect_db() 
        cursor = conn.cursor()  

        # Retrieve all student records from the students table.
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()  # This fetches all results after a successful query
        conn.close() 

        # Print each student's details.
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}, Address: {student[3]}")

    def delete_student(self, student_id): # Remove a student from the database using their student ID.

        conn = connect_db()  # Establish a connection to the database.
        cursor = conn.cursor()  # Create a cursor for executing SQL commands.

        # Execute a delete command to remove the student from the students table.
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        
        conn.commit()  # Commit the changes to save the deletion in the database.
        conn.close()  # Close the connection.

        # Inform the admin that the student has been removed successfully.
        print("Student removed successfully.")

    def search_student(self, student_id): #Search for a student in the database by their student ID.

        conn = connect_db()  # Connect to the database.
        cursor = conn.cursor()  # Create a cursor for executing SQL commands.

        # Execute a select query to find the student with the given ID.
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()  # Fetch the record of the student, if found.

        conn.close()  # Close the database connection.

        # Check if the student was found and print their details or notify if not found.
        if student:
            print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}, Address: {student[3]}")
        else:
            print("Student not found.")
