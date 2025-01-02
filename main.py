import os  # Importing the os module for file handling

# List to store student records
students = []


# Function to add a student
def add_student():
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")
    gpa = input("Enter student's gpa: ")

    # Adding student to the list
    students.append({'name': name, 'roll_number': roll_number, 'gpa': gpa})
    print(f"Student '{name}' added successfully!")


# Function to view all students
def view_students():
    if not students:
        print("No students to display.")
    else:
        print("\nStudent List:")
        for idx, student in enumerate(students, start=1):
            print(f"{idx}. {student['name']} - roll_number: {student['roll_number']}, gpa: {student['gpa']}")


# Function to search for a student by name
def search_student():
    name = input("Enter the student's name to search: ")
    found = False
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Found: {student['name']} - roll_number: {student['roll_number']}, gpa: {student['gpa']}")
            found = True
            break
    if not found:
        print(f"No student named '{name}' found.")


# Function to remove a student
def remove_student():
    name = input("Enter the student's name to remove: ")
    found = False
    for student in students:
        if student['name'].lower() == name.lower():
            students.remove(student)
            print(f"Student '{name}' removed successfully.")
            found = True
            break
    if not found:
        print(f"No student named '{name}' found to remove.")


# Function to save student data to a file
def save_students():
    try:
        with open("students.txt", "w") as file:
            for student in students:
                file.write(f"{student['name']},{student['roll_number']},{student['gpa']}\n")
        print("Student data saved to 'students.txt'.")
    except Exception as e:
        print(f"Error while saving data: {e}")


# Function to load student data from a file
def load_students(gpa=None):
    if os.path.exists("students.txt"):
        try:
            with open("students.txt", "r") as file:
                for line in file:
                    name, roll_number, grade = line.strip().split(',')
                    students.append({'name': name, 'roll_number': roll_number, 'gpa': gpa})
            print("Student data loaded successfully.")
        except Exception as e:
            print(f"Error while loading data: {e}")
    else:
        print("No saved student data found.")


# Main program loop
def main():
    load_students()  # Load saved student data when the program starts

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Remove Student")
        print("5. Save Students")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                search_student()
            elif choice == "4":
                remove_student()
            elif choice == "5":
                save_students()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
