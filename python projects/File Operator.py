import os
from datetime import datetime

file_name = "journal.txt"

def add_entry():
    entry = input("\nWrite your journal entry:\n")
    
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
    
    formatted_entry = f"\n{timestamp}\n{entry}\n---\n"
    
    with open(file_name, "a") as file:
        file.write(formatted_entry)
        
    print(" Entry saved with date and time!\n")
    
    
def view_entries():
    if not os.path.exists(file_name):
        print("No entries found.\n")
        return
    print("\nYour Journal Entries:\n")
    with open(file_name, "r") as file:
        print(file.read())
        
        
def search_entry():
    keyword = input(" Enter word to search: ").lower()
    found = False
    if not os.path.exists(file_name):
        print(" Journal file not found.\n")
        return
    with open(file_name, "r") as file:
        entries = file.read().split("---\n")
        for entry in entries:
            if keyword in entry.lower():
                print("\nMatch Found:\n" + entry.strip())
                found = True
    if not found:
        print(" No match found.\n")
        

def delete_all():
    if os.path.exists(file_name):
        os.remove(file_name)
        print(" All entries deleted!\n")
    else:
        print("Journal file doesn't exist.\n")
        

def menu():
    while True:
        print("\n Welcome to Personal Journal Manager!")    
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit\n")
        
        choice = input("Please select an option (1-5): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entry()
        elif choice == "4":
            delete_all()
        elif choice == "5":
            print(" Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()

          
          
            
        
            
          
  
    
        
    