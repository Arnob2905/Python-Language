people = []

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        super().show_details()
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def show_details(self):
        super().show_details()
        print(f"Department: {self.department}")


while True:
    print("\n--- Python OOP Project: Employee Management System ---\n")
    print("1. Add Person")
    print("2. Add Employee")
    print("3. Add Manager")
    print("4. Show All")
    print("5. Compare Salaries")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        p = Person(name, age)
        people.append(p)
        print(f"\nPerson created with name: {name} and age: {age}")

    elif choice == '2':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter salary: "))
        e = Employee(name, age, emp_id, salary)
        people.append(e)
        print(f"\nManager created with name:{name}, age:{age}, ID:{emp_id} and salary:${salary}")
        

    elif choice == '3':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter salary: "))
        dept = input("Enter department: ")
        m = Manager(name, age, emp_id, salary, dept)
        people.append(m)
        print(f"\nManager created with name:{name}, age:{age}, ID:{emp_id}, salary:${salary} and department:{dept}")
        

    elif choice == '4':
        if not people:
            print("\nNo people found.")
        else:
            print("\n--- All Records ---")
            for i, person in enumerate(people, 1):
                print(f"\n[{i}]")
                person.show_details()

    elif choice == '5':
        emps = [p for p in people if isinstance(p, Employee)]
        if len(emps) < 2:
            print("\nNot enough employees to compare.")
        else:
            print("\nSalary Comparisons:")
            for i in range(len(emps)):
                for j in range(i + 1, len(emps)):
                    a = emps[i]
                    b = emps[j]
                    print(f"\n{a.name} (ID: {a.emp_id}) - ${a.salary} vs {b.name} (ID: {b.emp_id}) - ${b.salary}")
                    if a.salary > b.salary:
                        print(f"{a.name} earns more.")
                    elif a.salary < b.salary:
                        print(f"{b.name} earns more.")
                    else:
                        print("Both have the same salary.")

    elif choice == '6':
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Try again.")


    



