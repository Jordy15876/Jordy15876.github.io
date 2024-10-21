# School Management System

## Overview
The School Management System is a Python application that facilitates the management of student records, offering functionalities tailored for admins, teachers, and students. This system streamlines educational administration and provides secure access to vital student information.

### Login Operation
Users can log in to their profiles using pre-configured credentials. This feature incorporates an authentication process to enhance the security of user data and access levels.

### CRUD Operations
- **Admin**: The admin user can:
  - Add new students
  - Update existing student information
  - Search for specific students
  - Delete student records

- **Teachers**: Teacher users can:
  - Add marks for students
  - View student records
  - Check marks for specific subjects

- **Students**: Student users can:
  - View their own profiles
  - View their marks

### Modular Design
The various components of the codebase have been modularized to facilitate testing and debugging. This design approach enhances maintainability and allows for focused updates to specific sections of the system.

## Limitations
This program was designed for the Secure Software Programming module at the University of Essex Online and includes several limitations that differ from the original design document:
- A SQL database has been implemented to ensure efficient execution and data management.
- Comprehensive security testing has not been performed, as the application is intended to run locally on the user's machine, meaning that extensive vulnerability assessments have not been conducted.
- The program is a foundational demonstration of functionality, and more complex operations are planned for future versions.

## Future Implementations
To enhance the School Management System, the following features are proposed for future development:
- **Enhanced Security**: Implement stronger password encryption, multi-factor authentication, and user role management to improve security.
- **Reporting Tools**: Develop a reporting module to generate academic performance reports and statistics for students and classes.
- **User Interface Improvements**: Create a graphical user interface (GUI) to provide a more user-friendly experience compared to the current command-line interface.
- **Integration with Learning Management Systems (LMS)**: Enable synchronization with popular LMS platforms to streamline educational processes and data sharing.
- **Real-Time Notifications**: Introduce a notification system to alert users about important updates, such as grades or attendance issues.
- **Data Backup and Recovery**: Incorporate features for regular data backups and recovery options to protect against data loss.

## Prerequisites
- Python 3.x
- SQLite (included with Python)
- Required packages: None (uses built-in libraries)


## Reference
Aarusheeeh (n.d.) School Management System Python MySQL. Available at: https://github.com/aarusheeeh/School-Management-System-Python-MySQL (Accessed: 24 September 2024).

Ankitsamaddar (n.d.) School Management PyQt. Available at: https://github.com/ankitsamaddar/school_management_pyqt (Accessed: 24 September 2024).

De Leon, J.J.B. (n.d.) School Management System. Available at: https://github.com/savjaylade84/school_management_system (Accessed: 24 September 2024).

GeeksforGeeks (n.d.) Python - Import module from different directory. Available at: https://www.geeksforgeeks.org/python-import-module-from-different-directory/ (Accessed: 23 September 2024).

ProgrammingKnowledge (2020) Python SQLite Tutorial - Create a Database in Python. Available at: https://www.youtube.com/watch?v=-mDKveRT_dA&list=PLNwaegOZi9pO1nE9dQMbsZL0JADavVO9A (Accessed: 24 September 2024).

Stack Overflow (2016) How to see a SQLite database content with Visual Studio Code. Available at: https://stackoverflow.com/questions/40993895/how-to-see-a-sqlite-database-content-with-visual-studio-code (Accessed: 24 September 2024).

Tomazic, N. (n.d.) Clean Code in Python. Available at: https://testdriven.io/blog/clean-code-python/ (Accessed: 23 September 2024).

