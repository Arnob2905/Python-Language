import os

def create_file(filename):

    try:
        with open(filename, 'x') as f:
            print(f"File '{filename}' created successfully!")
    except FileExistsError:
        print(f"File '{filename}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_to_file(filename, data):
   
    try:
        with open(filename, 'w') as f:
            f.write(data)
            print(f"Data written successfully to '{filename}'!")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_from_file(filename):
  
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"\nFile Content of '{filename}':")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
