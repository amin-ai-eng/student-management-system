# Student Management System

students = []
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print(f"{name} added successfully!")
    elif choice == "2":
        if len(students) ==0:
            print("No students found.")
        else:
            print("Student List:")
            for i, s in enumerate(students, 1):
                print(f"{i}. {s}")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
