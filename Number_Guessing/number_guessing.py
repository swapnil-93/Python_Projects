# Import random module to generate random values
import random
print ('{:#^50}'.format(" Welcome to Number Guessing Game "))
a = int(input("Enter First number: "))
b = int(input("Enter Last number: "))

number = random.randint(a , b)          # to generate a random integer number

chance = int(input("Enter the number of chances do you want for guessing: "))

# Try... Except until condition exist
try:
    while True:
        n = int(input("Enter a number: "))
        print ('*' * 20)
        print("Chance's Remaining !!! ", chance)
        print ()
        chance -= 1         # minus one chance after each repetition

        # if no chance is left
        if chance < 1:
            print('{:#^50}'.format(" Sorry, You Failed "))
            print('{:#^50}'.format(" Please Try Again !!! "))
            exit()

        # if the entered number is equal to guessing number
        if n == number:
            print('*' * 20)
            print("Congratulations, You have guessed it Correct!!!")
            print()
            break

        # if the entered number is less than guessing number
        elif n < number:
            print('*' * 20)
            print("Oops!, Number is Greater than entered number")
            print("Please try one more time!!")
            print()
            continue

        # if the entered number is greater than guessing number
        elif n > number:
            print('*' * 20)
            print("Oops!, Number is less than entered number")
            print("Please try one more time!!")
            print()
            continue

except:
    KeyboardInterrupt()

finally:
    print('_' * 50)
    print()
    print ('{:#^50}'.format(" Thank You for Playing "))
    print()
    print('{:#^50}'.format(" Please, Come again "))