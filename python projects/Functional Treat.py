data = [] 

def input_data():
    global data
    numbers = input("Enter numbers separated by spaces: ")
    data = list(map(int, numbers.split()))
    print("Data has been stored successfully!\n")

def display_summary():
    if not data:
        print("No data found. Please input data first.\n")
        return
    print("Data Summary:")
    print("Total elements:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum of all values:", sum(data))
    print()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def calculate_factorial():
    num = int(input("Enter a number to find its factorial: "))
    print("Factorial of", num, "is", factorial(num))
    print()

def filter_data():
    if not data:
        print("No data found. Please input data first.\n")
        return
    threshold = int(input("Enter threshold value: "))
    result = list(filter(lambda x: x > threshold, data))
    print("Filtered data (greater than", threshold, "):", result)
    print()

def sort_data():
    if not data:
        print("No data found. Please input data first.\n")
        return
    sorted_list = sorted(data)
    print("Sorted data:", sorted_list)
    print()

def show_statistics():
    if not data:
        print("No data found. Please input data first.\n")
        return
    total = sum(data)
    count = len(data)
    average = total / count
    print("Statistics:")
    print("Count:", count)
    print("Min:", min(data))
    print("Max:", max(data))
    print("Sum:", total)
    print("Average:", average)
    print()

# Main menu
while True:
    print("Welcome to the Data Analyzer and Transformer Program")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Statistics")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        input_data()
    elif choice == '2':
        display_summary()
    elif choice == '3':
        calculate_factorial()
    elif choice == '4':
        filter_data()
    elif choice == '5':
        sort_data()
    elif choice == '6':
        show_statistics()
    elif choice == '7':
        print("Thank you for using the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")