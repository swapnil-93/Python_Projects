import string
import random

def generator():
    s1 = string.ascii_uppercase     # this will generate uppercase string(A-Z)
    #print(s1)

    s2 = string.ascii_lowercase     # this will generate lowercase string(a-z)
    #print(s2)

    s3 = string.digits              # this will generate numbers from 0-9
    #print(s3)

    s4 = string.punctuation         # this will generate special characters
    #print(s4)

    pass_gen = int(input("Enter the password length:\n "))      # take the length of password to be generated from user

    # take elements form s1,s2,s3 and s4  and add it to the list
    l = []
    l.extend(list(s1))
    l.extend(list(s2))
    l.extend(list(s3))
    l.extend(list(s4))
    #print(l)

    random.shuffle(l)       # randomly shuffle the content of the list and give new list every time
    #print(l)

    pas = ("".join(l[0:pass_gen]))      # it will slice the randomly generated list from 0 to length and then we join it.
    print(pas)

generator()