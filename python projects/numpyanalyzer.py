import numpy as np

def create_array():
    print("\nSelect the type of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")
    choice = input("Enter choice: ")

    if choice == '1':
        data = input("Enter numbers: ").split()
        arr = np.array([int(i) for i in data])
    elif choice == '2':
        rows = int(input("Rows: "))
        cols = int(input("Cols: "))
        data = input(f"Enter {rows * cols} numbers: ").split()
        arr = np.array([int(i) for i in data]).reshape(rows, cols)
    elif choice == '3':
        d1, d2, d3 = map(int, input("Enter dimensions (x y z): ").split())
        data = input(f"Enter {d1*d2*d3} numbers: ").split()
        arr = np.array([int(i) for i in data]).reshape(d1, d2, d3)
    else:
        print("Invalid choice!")
        return None

    print("Created Array:\n", arr)
    return arr

def math_operation(arr):
    print("\nMath Operations:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    op = input("Choose: ")
    data = input(f"Enter {arr.size} numbers: ").split()
    other = np.array([int(i) for i in data]).reshape(arr.shape)

    if op == '1':
        print("Result:\n", arr + other)
    elif op == '2':
        print("Result:\n", arr - other)
    elif op == '3':
        print("Result:\n", arr * other)
    elif op == '4':
        print("Result:\n", arr / other)
    else:
        print("Invalid choice!")

def combine_arrays(arr):
    print("\nCombining Arrays")
    data = input(f"Enter {arr.size} numbers: ").split()
    new_arr = np.array([int(i) for i in data]).reshape(arr.shape)
    combined = np.vstack([arr, new_arr])
    print("Combined:\n", combined)

def sort_filter(arr):
    print("\n1. Sort\n2. Filter\n3. Search")
    ch = input("Choose: ")

    if ch == '1':
        print("Sorted row-wise:\n", np.sort(arr, axis=1))
    elif ch == '2':
        val = int(input("Filter values greater than: "))
        print("Filtered:\n", arr[arr > val])
    elif ch == '3':
        val = int(input("Enter value to search: "))
        loc = np.where(arr == val)
        print("Found at:", loc)
    else:
        print("Invalid choice!")

def statistics(arr):
    print("\n1. Sum\n2. Mean\n3. Median\n4. Std Dev\n5. Variance")
    ch = input("Choose: ")
    if ch == '1':
        print("Sum =", np.sum(arr))
    elif ch == '2':
        print("Mean =", np.mean(arr))
    elif ch == '3':
        print("Median =", np.median(arr))
    elif ch == '4':
        print("Std Dev =", np.std(arr))
    elif ch == '5':
        print("Variance =", np.var(arr))
    else:
        print("Invalid choice!")
        
array = None

while True:
    print("\n=== Welcome to the NumPy Analyzer ===")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Sort/Filter/Search Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")

    main_choice = input("Enter your choice: ")

    if main_choice == '1':
        array = create_array()
    elif main_choice == '2':
        if array is not None:
            math_operation(array)
        else:
            print("Create an array first!")
    elif main_choice == '3':
        if array is not None:
            combine_arrays(array)
        else:
            print("Create an array first!")
    elif main_choice == '4':
        if array is not None:
            sort_filter(array)
        else:
            print("Create an array first!")
    elif main_choice == '5':
        if array is not None:
            statistics(array)
        else:
            print("Create an array first!")
    elif main_choice == '6':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Try again.")