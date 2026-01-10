students = {}

def add_student(name, marks):
    students[name] = marks

def display_students():
    print("\nStudent Records:")
    for name, marks in students.items():
        print(name, ":", marks)

def main():
    print("STUDENT MANAGEMENT SYSTEM")

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Student Name: ")
            marks = int(input("Marks: "))
            add_student(name, marks)
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()