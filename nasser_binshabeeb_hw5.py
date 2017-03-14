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



def get_input():
    """
    Function that takes the input and checks if it's correct
    Args:
        None
    Return:
        None
    """
    
    for attempt in range(3):
        print("Please enter your PIN : ")
        value = input()
        print(value)
        if value == '1234':
            print("Your PIN is correct")
            exit(0)
        elif len(value) != 4:
            print("Invalid PIN length. Correct format is <9876> ")
        elif not value.isdigit():
            print("Incorerct PIN character. Correct format is <9876>")
        else:
            print("Your PIN is incorrect")

    print("Your account has been blocked")
    exit(1)



def main():
    """
    Main function:
    
    get_input: prompts for input and checks if the input matches PIN

        
    """
    #calling the get_input() definition
    get_input()


#call main, which calls everything needed
if __name__ == "__main__":
    main()
    exit(0)

