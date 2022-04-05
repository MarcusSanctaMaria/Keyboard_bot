import random
from random import randint

#List of random names
names = ["Mark", "Pheobe", "Ochre", "Jill", "Johnson", "Vector", "Kiara", "Louis", "Jodi", "Lily"]

def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message.
    Prameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Karlos' Kool Keyboards ***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you order your new Kool Keyboard ***")


def main():
    '''
    Purpose: To run all functions
    Prameters: None
    Returns: None
    '''

    welcome()

main()
