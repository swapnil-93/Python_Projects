# import all functions from the tkinter
from tkinter import *

# import messagebox class from tkinter
from tkinter import messagebox


# Function for clearing the
# contents of all text entry boxes
def clearAll():
    # deleting the content from the entry box
    day_entry.delete(0, END)
    month_entry.delete(0, END)
    year_entry.delete(0, END)
    givenday_entry.delete(0, END)
    givenmonth_entry.delete(0, END)
    givenyear_entry.delete(0, END)
    rsltday_entry.delete(0, END)
    rsltmonth_entry.delete(0, END)
    rsltyear_entry.delete(0, END)


# function for checking error
def checkError():
    # if any of the entry field is empty
    # then show an error message and clear
    # all the entries
    if (day_entry.get() == "" or month_entry.get() == ""
            or year_entry.get() == "" or givenday_entry.get() == ""
            or givenmonth_entry.get() == "" or givenyear_entry.get() == ""):
        # show the error message
        messagebox.showerror("Input Error")

        # clearAll function calling
        clearAll()

        return -1


# function to calculate Age
def calculateAge():
    # check for error
    value = checkError()

    # if error is occur then return
    if value == -1:
        return

    else:

        # take a value from the respective entry boxes
        # get method returns current text as string
        birth_day = int(day_entry.get())
        birth_month = int(month_entry.get())
        birth_year = int(year_entry.get())

        given_day = int(givenday_entry.get())
        given_month = int(givenmonth_entry.get())
        given_year = int(givenyear_entry.get())

        # if birth date is greater then given birth_month
        # then do not count this month and add 30 to the date so
        # as to subtract the date and get the remaining days
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if birth_day > given_day:
            given_month = given_month - 1
            given_day = given_day + month[birth_month - 1]

        # if birth month exceeds given month, then
        # do not count this year and add 12 to the
        # month so that we can subtract and find out
        # the difference
        if birth_month > given_month:
            given_year = given_year - 1
            given_month = given_month + 12

        # calculate day, month, year
        calculated_day = given_day - birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year

        # calculated day, month, year write back
        # to the respective entry boxes

        # insert method inserting the
        # value in the text entry box.

        rsltday_entry.insert(10, str(calculated_day))
        rsltmonth_entry.insert(10, str(calculated_month))
        rsltyear_entry.insert(10, str(calculated_year))

# Main program
if __name__ == "__main__":
    # Create a root window
    def close_window():
        root.destroy()
    root = Tk()

    # Set the background colour of root window
    root.configure(background="light blue")

    # set the name of tkinter root window
    root.title("Age Calculator")

    # Set the configuration of root window
    root.geometry("525x260")

    # Create a Date Of Birth : label
    dob = Label(root, text="Date Of Birth", bg="yellow")

    # Create a Given Date : label
    givenDate = Label(root, text="Given Date", bg="yellow")

    # Create a Day : label
    day = Label(root, text="Day", bg="light green")

    # Create a Month : label
    month = Label(root, text="Month", bg="light green")

    # Create a Year : label
    year = Label(root, text="Year", bg="light green")

    # Create a Given Day : label
    givenDay = Label(root, text="Given Day", bg="orange")

    # Create a Given Month : label
    givenMonth = Label(root, text="Given Month", bg="orange")

    # Create a Given Year : label
    givenYear = Label(root, text="Given Year", bg="orange")

    # Create a Years : label
    rsltYear = Label(root, text="Years", bg="light green")

    # Create a Months : label
    rsltMonth = Label(root, text="Months", bg="light green")

    # Create a Days : label
    rsltDay = Label(root, text="Days", bg="light green")

    # Create a Resultant Age Button and attached to calculateAge function
    resultantAge = Button(root, text="Resultant Age", fg="Black", bg="Red", command=calculateAge)

    # Create a Clear All Button and attached to clearAll function
    clearAllEntry = Button(root, text="Clear All", fg="Black", bg="Red", command=clearAll)
    exit = Button(root, text="Close", fg="Black", bg="Red", command=close_window)

    # Create a text entry box for filling or typing the information.
    day_entry = Entry(root)
    month_entry = Entry(root)
    year_entry = Entry(root)

    givenday_entry = Entry(root)
    givenmonth_entry = Entry(root)
    givenyear_entry = Entry(root)

    rsltyear_entry = Entry(root)
    rsltmonth_entry = Entry(root)
    rsltday_entry = Entry(root)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    dob.grid(row=0, column=1)

    day.grid(row=1, column=0)
    day_entry.grid(row=1, column=1)

    month.grid(row=2, column=0)
    month_entry.grid(row=2, column=1)

    year.grid(row=3, column=0)
    year_entry.grid(row=3, column=1)

    givenDate.grid(row=0, column=4)

    givenDay.grid(row=1, column=3)
    givenday_entry.grid(row=1, column=4)

    givenMonth.grid(row=2, column=3)
    givenmonth_entry.grid(row=2, column=4)

    givenYear.grid(row=3, column=3)
    givenyear_entry.grid(row=3, column=4)

    resultantAge.grid(row=4, column=2)

    rsltYear.grid(row=5, column=2)
    rsltyear_entry.grid(row=6, column=2)

    rsltMonth.grid(row=7, column=2)
    rsltmonth_entry.grid(row=8, column=2)

    rsltDay.grid(row=9, column=2)
    rsltday_entry.grid(row=10, column=2)

    clearAllEntry.grid(row=12, column=1)
    exit.grid(row=12, column=4)


    # Start the root
    root.mainloop()
