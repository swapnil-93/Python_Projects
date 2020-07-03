import os           # For operating system supported function
import platform     # Access Platform data

global std_list     # Global list for student name
std_list = ["Swapnil", "Rahul"]       # List of Student

# Writing a Function for management system
def Student():
    global bye      # making a global variable to use at the time of exit
    bye = "\nThank you for using our Student Management System"   # message to be printed after exit
    # Simple welcome formatting
    print ("#### Welcome to Student Management System ####")
    print ("""**********************************************
    
    Enter 1 : To view list of Student's
    -----------------------------------
    Enter 2 : To add new student
    -----------------------------------
    Enter 3 : To search student in list
    -----------------------------------
    Enter 4 : To delete student from list
    ------------------------------------
    """)
    # use try except for validation and error handling
    try :
        user = int(input("Please select an option: "))
    except ValueError:      # for checking if value is number or not
        exit("\n Please enter a number!!")  # Error message will occure when value other than number is entered
    else:
        print("\n") # print new line

    # Code for menu
    if(user == 1):  # if value is 1 it will print list of students
        print("List of Student's")
        print("--------------------")
        for students in std_list:
            print("==> {}".format(students))     # names of students will be printed
    elif(user == 2): # if value is 2 we can add new student into record
        add_std = input("Enter name of student: ")      # Enter name of student to be added
        if add_std in std_list:
            print ("\n This student {} is already in the database".format(add_std)) # if student is already present
        else:
            std_list.append(add_std)        # if new student then it will apend the name into list
            print("\n New student {} added successfully \n". format(add_std))
            for students in std_list:
                print("==>{}".format(students))     # print the list with updated names
    elif(user == 3): # if value is 3 we can search for student in database
        search = input("Enter name of student: ")       # Enter name of student
        if search in std_list:          # Check if student is  present in the list
            print("\n==> Record found of {}".format(search))
        else:
            print("\n==> No record found of {}".format(search))     # if student is not present in the list
    elif(user == 4): # if value is 4 you can delete an existing student data
        delete = input("Enter name of student you want to delete")  # enter name you want to delete
        if delete in std_list:      # check if name is in the list
            std_list.remove(delete) # if yes then delete the name using remove function
            print("\n==> Record of {} successfully deleted \n".format(delete))
            for students in std_list:
                print("==>{}".format(students))     # Print updated list
        else:
            print ("\n==> No Record found for {}".format(delete))   # if name is not in the list

    elif(user <1 or user >4): # validation of user option i.e the number entered by user are between 1 to 4
        print("Please enter valid option ")     # if no then this message will pop

# if we want to run our project only once
Student()

#program for continuous loop
def looping():
    run =  input("\n Do you want to Run Again Y/n: ") #  Y to run program again and n to exit
    if run.lower() == 'y':              # it will check if value entered  is 'y'
        if platform.system() == "Windows":  # here 'platform' module is used to check if os is windows
            print(os.system('cls'))     # here 'os' module is used to clear the console window
        else:
            print(os.system('clear')) # if platform is other than windows i.e. Linux
        Student()       # call our student function
        looping()       # call looping to run continuously
    else:
        quit(bye)           # if value is n then progam will stop
looping()