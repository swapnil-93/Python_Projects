# creating  lists of users, their PINs and bank statements
users = ['user1', 'user2', 'user3']     # List of User
pins = [1234, 2222, 3333]               # List of PIN
amounts = [1000, 2000, 3000]            # List of Account Balance
count = 0

# while loop checks existence of the entered username
while True:
    print('*' * 50)     # ('*' * 50) - 50 times *
    print ('{:#^50}'.format(' Welcome to Python base ATM System '))
    print('*' * 50)
    user = input('\nEnter User Name: ')
    user = user.lower()
    if user in users:
        if user == users[0]:
            print ('Welcome, to Python ATM ', str.capitalize(users[0]))
            n = 0
        elif user == users[1]:
            print('Welcome, to Python ATM ', str.capitalize(users[1]))
            n = 1
        elif user == users[2]:
            print('Welcome, to Python ATM ', str.capitalize(users[2]))
            n = 2
        break
    else:
        print('-' * 20)
        print('{:#^20}'.format('Invalid Username'))
        print('-' * 20)

# comparing pin
while count < 3:
    print('*' * 20)
    pin = int(input('Please Enter PIN: '))      # Enter your Pin
    print('*' * 20)
    if user == users[0]:                        # Check for User
        if pin == pins[0]:                      # Check for PIN of specified User
            break
        else:
            count += 1
            print('*' * 10)
            print('{:#^20}'.format('Invalid PIN'))      # if PIN is wrong
            print('*' * 10)
            print()
    elif user == users[1]:
        if pin == pins[1]:
            break
        else:
            count += 1
            print('*' * 10)
            print('{:#^20}'.format('Invalid PIN'))
            print('*' * 10)
            print()
    elif user == users[2]:
        if pin == pins[2]:
            break
        else:
            count += 1
            print('*' * 10)
            print('{:#^20}'.format('Invalid PIN'))
            print('*' * 10)
            print()

# in case of a valid pin- continuing, or exiting
if count == 3:                      # if You enter wrong pins 3 times
    print('*' * 20)
    print('{:#^30}'.format('Three Unsuccessful Pin Attempts'))
    print('{:!^30}'.format('Your Cards Has been Locked'))
    print('*' * 20)
    exit()

print('-' * 20)
print('{:#^40}'.format('Login Successful, Continue'))
print('-' * 20)
print()
print('-' * 20)
print(str.capitalize(users[n]), 'Welcome to ATM')
print('-' * 20)
print('{:$^30}'.format('Python ATM System'))

# Main menu
while True:
    print('-' * 20)
    response = input(
        'Select Your Choice: \nStatement__(S) \nWithdraw___(W) \nDeposite__(D)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
    print('-' * 20)
    valid_responses = ['s', 'w', 'd', 'p', 'q']
    response = response.lower()
    if response == 's':
        print('-' * 30)
        print(str.capitalize(users[n]), 'Your account balance is:  ', amounts[n], 'Rs.')
        print('-' * 30)

    elif response == 'w':
        print('-' * 30)
        cash_out = int(input('Please Enter Amount You Want to Withdraw: '))
        print('-' * 30)
        if cash_out % 100 != 0:         # Check if Entered amount is divisible by 100
            print('-' * 30)
            print('Amount Should be in Multiple of 100')
            print('-' * 30)
        elif cash_out > amounts[n]:     # Check if enter amount is greater than your account balance
            print('-' * 30)
            print('You Have Insufficient Balance in your Account')
            print('-' * 30)
        else:
            amounts[n] = amounts[n] - cash_out      # If condition satisfies then deduted the entered amount from original balance
            print('-' * 30)
            print('Your Updated account balance is: ', amounts[n], 'Rs.')
            print('-' * 30)

    elif response == 'd':
        print()
        print('-' * 30)
        cash_in = int(input('Enter Amount you want to Deposit: '))
        print('-' * 30)
        print()
        if cash_in % 100 != 0:
            print('-' * 30)
            print('Amount Should be in Multiple of 100')
            print('-' * 30)
        else:
            amounts[n] = amounts[n] + cash_in
            print('-' * 30)
            print('Your Updated account balance is: ', amounts[n], 'Rs.')
            print('-' * 30)
    elif response == 'p':
        print('-' * 30)
        new_pin = int(input('Please Enter New PIN: '))
        print('-' * 30)
        if new_pin != pins[n] :
            print('-' * 30)
            new_ppin = int(input('Please Confirm New PIN: '))
            print('-' * 30)
            if new_ppin != new_pin:
                print('-' * 30)
                print('PIN Does not Match')
                print('-' * 30)
            else:
                pins[n] = new_pin
                print('PIN Successfully Changed!!!')
        else:
            print('-' * 30)
            print('New PIN Must Consist Of 4 Digits \nand  Must be Different From Previous PIN')
            print('-' * 30)
    elif response == 'q':
        exit()
    else:
        print('-' * 30)
        print('Please Enter a Valid Response')
        print('-' * 30)
