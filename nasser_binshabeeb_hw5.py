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



count = 3

while count:
    count = count - 1
    print("Please enter your PIN :")
    if input() == '1234':
        print("Your PIN is correct")
        exit(0)
    print("Your PIN is incorrect")

print("You account has been blocked")


exit(1)

