# With User Defined Functions
students = []

def add_student():
    print("\nEnter student details:")
    student_id = input("Student ID: ")
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    date_of_birth = input("Date of Birth (YYYY-MM-DD): ")
    subjects = input("Subjects (comma-separated): ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade,
        "date_of_birth": date_of_birth,
        "subjects": subjects
    }

    students.append(student)
    print("\nStudent Added Successfully!")

def display_students():
    print("\nDisplay All Students")
    if not students:
        print("No student records available.")
    for s in students:
        print(f"Student ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {s['subjects']}")

def update_student_information():
    usi = input("Enter Student ID to update: ")
    for s in students:
        if s["id"] == usi:
            print("What do you want to update?")
            print("1. Age")
            print("2. Subjects")
            update_choice = input("Enter your choice: ")

            if update_choice == '1':
                s["age"] = input("Enter new age: ")
                print("Age Updated.")
            elif update_choice == '2':
                s["subjects"] = input("Enter new subjects (comma-separated): ")
                print("Subjects Updated.")
            else:
                print("Invalid update option.")
            break
    else:
        print("Student ID not found.")

def delete_student():
    usi = input("Enter Student ID to delete: ")
    for i, s in enumerate(students):
       if s["id"] == usi:
            del students[i]
            print("Student ID Deleted.")
            break
    else:
        print("Student ID not found.")

def display_subjects():
    subjects_list = []
    for student in students:
        subjects = student["subjects"].split(",")
        for subject in subjects:
            subject = subject.strip()
        if subject and subject not in subjects_list:
                subjects_list.append(subject)
    print("Subjects Offered:", ", ".join(subjects_list))

print("------Welcome to the Student Data Organizer!------")

while True:
    print("""
    Select an option:
    1. Add Student
    2. Display All Students
    3. Update Student Information
    4. Delete Student
    5. Display Subjects Offered
    6. Exit
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        update_student_information()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        display_subjects()
    elif choice == '6':
        print("Thank you!\nProgram Exited..........")
        break
    else:
        print("Invalid choice. Please try again.")

    


    
# Without User-Defined Functions   

students = []

print("------Welcome to the Student Data Organizer!------")

while True:
    print("""
    Select an option:
    1. Add Student
    2. Display All Students
    3. Update Student Information
    4. Delete Student
    5. Display Subjects Offered
    6. Exit
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nEnter student details:")
        student_id = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        date_of_birth = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "date_of_birth": date_of_birth,
            "subjects": subjects
        }

        students.append(student)
        print("\nStudent Added Successfully!")

    elif choice == '2':
        print("\nDisplay All Students")
        if not students:
            print("No student records available.")
        else:
            for s in students:
                print(f"Student ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {s['subjects']}")

    elif choice == '3':
        usi = input("Enter Student ID to update: ")
        found = False
        for s in students:
            if s["id"] == usi:
                print("What do you want to update?")
                print("1. Age")
                print("2. Subjects")
                update_choice = input("Enter your choice: ")

                if update_choice == '1':
                    s["age"] = input("Enter new age: ")
                    print("Age Updated.")
                elif update_choice == '2':
                    s["subjects"] = input("Enter new subjects (comma-separated): ")
                    print("Subjects Updated.")
                else:
                    print("Invalid update option.")
                found = True
                break
        if not found:
            print("Student ID not found.")

    elif choice == '4':
        usi = input("Enter Student ID to delete: ")
        found = False
        for i, s in enumerate(students):
            if s["id"] == usi:
                del students[i]
                print("Student ID Deleted.")
                found = True
                break
        if not found:
            print("Student ID not found.")

    elif choice == '5':
        subjects_list = []
        for student in students:
            subject_items = student["subjects"].split(",")
            for subject in subject_items:
                subject = subject.strip()
                if subject and subject not in subjects_list:
                    subjects_list.append(subject)
        print("Subjects Offered:", ", ".join(subjects_list))

    elif choice == '6':
        print("Thank you!\nProgram Exited..........")
        break

    else:
        print("Invalid choice. Please try again.") 
    
    
    