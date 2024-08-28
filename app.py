import os
import pandas as pd
from enum import Enum

# Define your Enum for selection options
class Selection(Enum):
    BUSINESS_FINANCIAL = 1
    CUSTOMERS_100 = 2
    ORGANIZATIONS_100 = 3
    EXIT = 4
    CLEAR_SCREEN = 5
    SHOW_ALL = 6
    SHOW_HEAD = 7
    SHOW_TAIL = 8

# Define file paths
FILE_PATHS = {
    Selection.BUSINESS_FINANCIAL: r"D:\JohnBryce\CSVDatasets\business-financial-data-march-2024-csv.csv",
    Selection.CUSTOMERS_100: r"D:\JohnBryce\CSVDatasets\customers-100.csv",
    Selection.ORGANIZATIONS_100: r"D:\JohnBryce\CSVDatasets\organizations-100.csv"
}

# Function to display the main menu options
def menu():
    for item in Selection:
        if item not in [Selection.SHOW_ALL, Selection.SHOW_HEAD, Selection.SHOW_TAIL]:
            print(f'{item.value} - {item.name.replace("_", " ").title()}')
    return Selection(int(input("What information do you want? ")))

# Function to show detailed information based on the selection
def show_info(option):
    if option in FILE_PATHS:
        print("1 - Show All Information")
        print("2 - Show Head (First 5 lines)")
        print("3 - Show Tail (Last 5 lines)")
        choice = int(input("Select an option: "))
        if choice == 1:
            return Selection.SHOW_ALL
        elif choice == 2:
            return Selection.SHOW_HEAD
        elif choice == 3:
            return Selection.SHOW_TAIL
        else:
            print("Invalid option selected.")
            return None


# Function to process the file based on user choice
def process_file(option, file_option):
    file_path = FILE_PATHS.get(option)
    if file_path:
        try:
            df = pd.read_csv(file_path)  # Read the CSV file using pandas

            if file_option == Selection.SHOW_ALL:
                print("Displaying all information:")
                print(df)  # Show all information
            elif file_option == Selection.SHOW_HEAD:
                print("Displaying the first 5 lines of the file:")
                print(df.head(5))  # Show the first 5 lines
            elif file_option == Selection.SHOW_TAIL:
                print("Displaying the last 5 lines of the file:")
                print(df.tail(5))  # Show the last 5 lines
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print("File path not found.")

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main loop for the application
if __name__ == "__main__":
    while True:
        user_selection = menu()
        if user_selection == Selection.EXIT:
            exit()
        elif user_selection == Selection.CLEAR_SCREEN:
            clear_screen()
        elif user_selection in [Selection.BUSINESS_FINANCIAL, Selection.CUSTOMERS_100, Selection.ORGANIZATIONS_100]:
            sub_selection = show_info(user_selection)
            if sub_selection:
                process_file(user_selection, sub_selection)
        else:
            print("Invalid selection. Please try again.")
