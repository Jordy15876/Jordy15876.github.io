from database import create_tables
from Users.admin import Admin
from Users.teacher import Teacher
from Users.student import Student

def login(users):
    """This will authenticate the different users with username and password.

    This function prompts the user to input their username and password.
    It loops through the provided list of users (Admin, Teacher, and Student)
    to check if any user’s credentials match the input. If a match is found,
    the user is logged in and returned. If not, an error message is displayed.

    Args:
        users (list): A list of user objects (Admin, Teacher, Student).

    Returns:
        User: The authenticated user object if login is successful, otherwise None.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Loop through each user to check if credentials match
    for user in users:
        if user.authenticate(username, password):
            print(f"Welcome, {username}!")
            return user
    
    # If no match is found, inform the user and return None
    print("Invalid username or password.")
    return None

def main():
    """This is the point which starts the entire program.

    This function initializes the system by creating necessary database tables and 
    sets up instances of Admin, Teachers, and Students. Depending on the logged-in
    user's role, it directs the user to different functionality: Admin, Teacher, or
    Student. Each role has specific actions they can perform within the system.
    """
    create_tables()  # This will ensure that the tables are created before the program initializes.
    logged_in_user = None

    # Create an Admin user instance
    admin_user = Admin("admin", "adminpassword")
    
  # This will create initial users in the database for the use of the program.
    teachers = [
        Teacher("john.doe", "teacherpassword", "Mathematics", 7),
        Teacher("jane.smith", "teacherpassword", "English", 9),
        Teacher("michael.johnson", "teacherpassword", "Science", 12),
        Teacher("emily.brown", "teacherpassword", "Art", 13),
        Teacher("william.jones", "teacherpassword", "Physical Education", 10)
    ]

    # Student data (student_id, name, grade, address)
    students_data = [
        ("001", "Michael Brown", 7, "234 Teak Way, Barbican Terrace"),
        ("002", "Emma Wilson", 8, "456 Oak St, Harbor View"),
        ("003", "Olivia Davis", 7, "789 Pine St, Cherry Gardens"),
        ("004", "James White", 9, "321 Elm St, Old Hope Road"),
        ("005", "Lucas Martinez", 7, "654 Cedar St, Constant Spring"),
        ("006", "Ava Johnson", 8, "987 Birch St, Musgrave Road"),
        ("007", "Ethan Lee", 7, "147 Walnut St, Emancipation Park Ave"),
        ("008", "Isabella Rodriguez", 7, "258 Fir St, Springfield"),
    ]

    # Add students to the database via the Admin user
    for student_data in students_data:
        admin_user.add_student(*student_data)

    # Create Student instances with their respective credentials
    student_users = [Student(student[0], "studentpassword") for student in students_data]

    # Main program loop to keep the application running and interact with users
    while True:
        print("\nWelcome to the School Management System")
        
        # Authenticate the user (Admin, Teacher, or Student)
        logged_in_user = login([admin_user] + teachers + student_users)

        if logged_in_user:
            # If the logged-in user is an Admin
            if isinstance(logged_in_user, Admin):
                while True:
                    print("\nAdmin Menu:")
                    print("1. View Students")
                    print("2. Add Student")
                    print("3. Edit Student")
                    print("4. Delete Student")
                    print("5. Search Student")
                    print("6. Logout")
                    choice = input("Enter your choice: ")
                    
                    # Admin functionalities based on user input
                    if choice == "1":
                        logged_in_user.view_students()
                    elif choice == "2":
                        student_id = input("Enter Student ID: ")
                        name = input("Enter Student Name: ")
                        grade = input("Enter Student Grade: ")
                        address = input("Enter Student Address: ")
                        logged_in_user.add_student(student_id, name, grade, address)
                    elif choice == "3":
                        student_id = input("Enter Student ID to edit: ")
                        name = input("Enter new name (leave blank to skip): ")
                        grade = input("Enter new grade (leave blank to skip): ")
                        address = input("Enter new address (leave blank to skip): ")
                        kwargs = {k: v for k, v in zip(['name', 'grade', 'address'], [name, grade, address]) if v}
                        logged_in_user.edit_student(student_id, **kwargs)
                    elif choice == "4":
                        student_id = input("Enter Student ID to delete: ")
                        logged_in_user.delete_student(student_id)
                    elif choice == "5":
                        student_id = input("Enter Student ID to search: ")
                        logged_in_user.search_student(student_id)
                    elif choice == "6":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")

            # If the logged-in user is a Teacher
            elif isinstance(logged_in_user, Teacher):
                while True:
                    print("\nTeacher Menu:")
                    print("1. View Students in Your Grade")
                    print("2. Add Marks")
                    print("3. Edit Marks")
                    print("4. View Subject")
                    print("5. View Marks")
                    print("6. Logout")
                    choice = input("Enter your choice: ")
                    
                    # Teacher functionalities based on user input
                    if choice == "1":
                        logged_in_user.view_student_records()
                    elif choice == "2":
                        student_id = input("Enter Student ID: ")
                        marks = input("Enter Marks: ")
                        logged_in_user.add_marks(student_id, marks)
                    elif choice == "3":
                        student_id = input("Enter Student ID: ")
                        marks = input("Enter new Marks: ")
                        logged_in_user.edit_marks(student_id, marks)
                    elif choice == "4":
                        logged_in_user.view_subject()
                    elif choice == "5":
                        logged_in_user.view_marks()
                    elif choice == "6":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")

            # If the logged-in user is a Student
            elif isinstance(logged_in_user, Student):
                while True:
                    print("\nStudent Menu:")
                    print("1. View Profile")
                    print("2. View Marks")
                    print("3. Logout")
                    choice = input("Enter your choice: ")
                    
                    # Student functionalities based on user input
                    if choice == "1":
                        logged_in_user.view_profile()
                    elif choice == "2":
                        logged_in_user.view_marks()
                    elif choice == "3":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
