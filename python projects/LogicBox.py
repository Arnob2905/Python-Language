# With User-Defined Function

print(" Welcome to the Pattern Generator and Number Analyzer !")

def print_menu():
    print("""
    Select an option:
    1. Generate a Pattern
    2. Analyze a Range of Numbers
    3. Exit
    """)

def rightangled_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

def pyramid(rows):
    for i in range(1, rows + 1):
        print(("*" * (2 * i - 1)).center(2 * rows - 1))

def leftangled_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)

def diamond(rows):
    # Top
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    # Bottom
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

def pattern_generator():
    print("\n Choose a pattern type:")
    print(" 1. Right-angled Triangle")
    print(" 2. Pyramid")
    print(" 3. Left-angled Triangle")
    print(" 4. Diamond ")

    pattern_choice = input("Enter your choice: ")
    rows_str = input("Enter number of rows: ")
    if rows_str.isdigit():
        rows = int(rows_str)
        if rows <= 0:
            print("Please enter a positive number of rows.")
            return
        if pattern_choice == '1':
            rightangled_triangle(rows)
        elif pattern_choice == '2':
            pyramid(rows)
        elif pattern_choice == '3':
            leftangled_triangle(rows)
        elif pattern_choice == '4':
            diamond(rows)
        else:
            print("Invalid pattern choice.")
    else:
        print("Invalid input. Please enter an integer for the number of rows.")


def number_analyzer():
    start = int(input("Enter start of the range :"))
    end  = int(input("Enter end of the range :"))
    count = 0
    
    for i in range (start,end + 1):
        if i % 2 == 0:
            print(f"Number {i} is Even")
        else:
            print(f"Number {i} is Odd")
        count += i    
    print(f"Sum of all numbers from {start} to {end} is : {count}")
        
    

print_menu()
choice = input("Enter your choice: ")        

if choice == '1':
    pattern_generator()
elif choice == '2':
    number_analyzer()
elif choice == '3':
    print("\nExiting program.")
else:
    print("\nInvalid menu choice.")




# Without User Defined Function

print(" Welcome to the Pattern Generator and Number Analyzer !")

print("""
    Select an option:
    1. Generate a Pattern
    2. Analyze a Range of Numbers
    3. Exit
""")

choice = input("Enter your choice: ")

if choice == '1':
    print("\n Choose a pattern type:")
    print(" 1. Right-angled Triangle")
    print(" 2. Pyramid")
    print(" 3. Left-angled Triangle")
    print(" 4. Diamond ")

    pattern_choice = input("Enter your choice: ")
    rows_str = input("Enter number of rows: ")

    if rows_str.isdigit():
        rows = int(rows_str)
        if rows <= 0:
            print("Please enter a positive number of rows.")
        else:
            if pattern_choice == '1':
                for i in range(1, rows + 1):
                    print("*" * i)
            elif pattern_choice == '2':
                for i in range(1, rows + 1):
                    print(("*" * (2 * i - 1)).center(2 * rows - 1))
            elif pattern_choice == '3':
                for i in range(1, rows + 1):
                    print(" " * (rows - i) + "*" * i)
            elif pattern_choice == '4':
                # Top
                for i in range(1, rows + 1):
                    print(" " * (rows - i) + "*" * (2 * i - 1))
                # Bottom
                for i in range(rows - 1, 0, -1):
                    print(" " * (rows - i) + "*" * (2 * i - 1))
            else:
                print("Invalid pattern choice.")
    else:
        print("Invalid input. Please enter an integer for the number of rows.")

elif choice == '2':
    start = int(input("Enter start of the range :"))
    end = int(input("Enter end of the range :"))
    count = 0

    for i in range(start, end + 1):
        if i % 2 == 0:
            print(f"Number {i} is Even")
        else:
            print(f"Number {i} is Odd")
        count += i
    print(f"Sum of all numbers from {start} to {end} is : {count}")

elif choice == '3':
    print("\nExiting program.")
else:
    print("\nInvalid menu choice.")

