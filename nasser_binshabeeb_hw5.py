#!/usr/bin/env python3

#################################################
#
# Name : Nasser Binshabeeb
# 
#
# Project Info : Python
#
#
#################################################


#import sys


count = 3

def main():
    """
    Main function: Check if the user has entered the correct password
    Args:
        None
    Return:
        None
        
    """
    get_input(1234)



def get_input(value):
    """
    Function that takes the input and checks if it's correct
    Args:
        value:use input
    Return:
        None
    """
    while count:
        count = count - 1
        print("Please enter your PIN : ")
        if value == 1234:
            print("Your PIN is correct")
            exit(0)
        elif len(value) != 4:
            print("Invalid PIN length. Correct format is <9876> ")
        elif not value.isdigit():
            print("Incorerct PIN character. Correct format is <9876>")
        else:
            #do something
            print("Your PIN is incorrect")
    print("Your account has been blocked")
    exit(1)



if __name__ == "__main__":
    main()
    exit(0)

