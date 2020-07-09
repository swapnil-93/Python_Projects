# Import tkinter
from tkinter import *

# Class for loan calculator
class LoanCalculator:

    def __init__(self):
        root = Tk()  # Create a window
        root.title("Loan Calculator")  # Set title
        # create the input boxes.
        Label(root, text="Annual Interest Rate").grid(row=1, column=1)
        Label(root, text="Number of Years").grid(row=2, column=1)
        Label(root, text="Loan Amount").grid(row=3, column=1)
        Label(root, text="Monthly Payment").grid(row=1, column=3)
        Label(root, text="Total Payment").grid(row=2, column=3)

        # for taking inputs
        self.annualInterestRateVar = StringVar()
        Entry(root, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)
        self.numberOfYearsVar = StringVar()

        Entry(root, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()

        Entry(root, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar = StringVar()

        lblMonthlyPayment = Label(root, textvariable= self.monthlyPaymentVar).grid(row=1, column=4)

        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(root, textvariable= self.totalPaymentVar).grid(row=2, column=4)

        # create the button
        btComputePayment = Button(root, text="Compute Payment", command=self.computePayment).grid( row=6, column=2)
        root.mainloop()  # Create an event loop

    # compute the total payment.
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
                       * int(self.numberOfYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        # compute the monthly payment.
        monthlyPayment = loanAmount * monthlyInterestRate / (1
                                                             - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment
        root = Tk()  # create the widget


# call the class to run the program.
LoanCalculator()