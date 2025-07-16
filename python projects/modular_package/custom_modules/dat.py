from datetime import datetime, timedelta

def display_current_datetime():
 
    now = datetime.now()
    print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_date_difference(date1_str, date2_str):
   
    try:
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')
        difference = abs((date2 - date1).days)
        print(f"Difference: {difference} days")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
    except Exception as e:
        print(f"An error occurred: {e}")

