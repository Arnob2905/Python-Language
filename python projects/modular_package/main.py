from custom_modules import dat
from custom_modules import file_ops
from custom_modules import math_utils
from custom_modules import random_module
from custom_modules import uuid_module

def display_main_menu():

    print("\n================================")
    print("Welcome to Multi-Utility Toolkit")
    print("================================")
    print("Choose an option:")
    print("1. Datetime Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations")
    print("6. Exit")
    print("================================")

def handle_datetime_operations():
   
    while True:
        print("\nDatetime Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            dat.display_current_datetime()
        elif choice == '2':
            date1_str = input("Enter the first date (YYYY-MM-DD): ")
            date2_str = input("Enter the second date (YYYY-MM-DD): ")
            dat.calculate_date_difference(date1_str, date2_str)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def handle_math_operations():
  
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Calculate Compound Interest")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                num = int(input("Enter a number: "))
                print(f"Factorial: {math_utils.calculate_factorial(num)}")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == '2':
            try:
                principal = float(input("Enter principal amount: "))
                rate = float(input("Enter rate of interest (in %): "))
                time_years = float(input("Enter time (in years): "))
                print(f"Compound Interest: {math_utils.calculate_compound_interest(principal, rate, time_years):.2f}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def handle_random_operations():
    
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random Password")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Generated Random Number: {random_module.generate_random_number(1, 100)}")
        elif choice == '2':
            try:
                length = int(input("Enter password length: "))
                print(f"Generated Password: {random_module.generate_random_password(length)}")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def handle_uuid_operations():
   
    while True:
        print("\nGenerate Unique Identifiers:")
        print("1. Generate UUID1")
        print("2. Generate UUID4")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Generated UUID1: {uuid_module.generate_uuid1()}")
        elif choice == '2':
            print(f"Generated UUID4: {uuid_module.generate_uuid4()}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def handle_file_operations():
   
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter file name: ")
            file_ops.create_file(filename)
        elif choice == '2':
            filename = input("Enter file name: ")
            data = input("Enter data to write: ")
            file_ops.write_to_file(filename, data)
        elif choice == '3':
            filename = input("Enter file name: ")
            file_ops.read_from_file(filename)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            handle_datetime_operations()
        elif choice == '2':
            handle_math_operations()
        elif choice == '3':
            handle_random_operations()
        elif choice == '4':
            handle_uuid_operations()
        elif choice == '5':
            handle_file_operations()
        elif choice == '6':
            print("Exiting Multi-Utility Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
