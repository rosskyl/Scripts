#Author: Kyle Ross
#Date: 2/16/2016
#Purpose: validate an input

#sources
#"Automate the Boring Stuff with Python" by Al Sweigart

import re

def isValidInput(string):
    #length greater than 50 not allowed
    if len(string) > 50:
        return False
    #valid characters are letters, digists, !, ., ?, @, #, $, %, ^, &, *, and ,
    regex = re.compile(r"[\w!.?@#$%^&*,]+")
    search = regex.search(string).group()

    return string == search

username = input("Enter the username: ")
if isValidInput(username):
    print("Valid input")
else:
    print("Invalid input")
