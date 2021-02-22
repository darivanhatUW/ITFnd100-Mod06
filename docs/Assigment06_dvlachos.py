# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030, Created started script
# RRoot,1.1.2030, Added code to complete assignment 5
# Dvlachos,2.17.2021, Modified code to complete assignment 6
# Dvlachos,2.21.2021, Restructured code to eliminate the user of global variables
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
list_of_rows = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
str_task = ""  # Captures the user task data
str_priority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.title().strip(), "Priority": priority.lower().strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(str_task, str_priority, list_of_rows):
        """ Puts data into dictionary rows, then appends the rows to table called list_of_rows

        :param str_task: (string) with name of task:
        :param str_priority: (string) with level of priority:
        :return: (list) of dictionary rows
        """
        dicRow = {"Task": str_task.title(), "Priority": str_priority.lower().strip()}  # Adds the user input in the dictionary
        list_of_rows.append(dicRow)  # Appends the new user input to the table
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(remove_task, list_of_rows):
        """ Removes data from the list_of_rows

        :param remove_task: (string)
        :param list_of_rows:
        :return: (list) of dictionary rows
        """
        for row in list_of_rows:
            if row["Task"] == remove_task:
                list_of_rows.remove(row)
                print(remove_task, " deleted.")
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes the data to the file from the list_of_rows

        :param file_name: (object) saved as .txt:
        :param list_of_rows: (list) of dictionary rows:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "w")  # Opens the "ToDoFile.txt"
        for row in list_of_rows: # Adds items from table to text file
            file.write(row["Task"] + ", " + row["Priority"] + "\n")
            print(row["Task"] + "(" + row["Priority"] + ")")
        file.close()
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Prompt to add a new task and priority from user input

        :return: strings
        """
        str_task = (input("Which task would you like to add? ")).title()  # Ask the user to input a task
        str_priority = (input("What is its priority? (Choose: high, medium, low) ")).lower()  # user input priority level
        return str_task, str_priority


    @staticmethod
    def input_task_to_remove():
        """ Prompt to delete task from user input

        :return: string
        """
        remove_task = (input("What task would you like removed? ")).title()
        return remove_task
        # return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name, list_of_rows)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(list_of_rows)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        str_task, str_priority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(str_task, str_priority, list_of_rows)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        IO.input_task_to_remove()
        list_of_rows, strStatus = Processor.remove_data_from_list(str_task, list_of_rows)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(file_name, list_of_rows)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(file_name, list_of_rows)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
