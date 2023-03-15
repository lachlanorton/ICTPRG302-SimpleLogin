# Welcome to "The Python Playground"
# This space is used for experimentation of code
# For actual assessment file, please refer to simplelogin.py
# Author: Lachlan Orton
# Date: 15/03/2023
# TAFE NSW St. Leonard's / Programming and Data

import time

accounts = open("accounts.txt", "r")
print(accounts.readlines())

# runningProgram = True

# Initial attempt at basic menu functionality
#
# print("A) LOGIN")
# print("B) REGISTER")
# print("C) SAVE ACCOUNTS FILE")
# print("D) VIEW ACCOUNTS FILE")
# print("E) EXIT")
# menuChoice = input("Please select an option: ")
# if menuChoice == "A" or "a":
#     print("\nPlease enter your details to login.")
# elif menuChoice == "B" or "b":
#     print("\nPlease enter new details to register.")
# elif menuChoice == "C" or "c":
#     print("\nSaving and closing accounts file.")
# elif menuChoice == "D" or "d":
#     print(accounts.read())
# elif menuChoice == "E" or "e":
#     print("Exiting...")
# else:
#     print("Invalid option! Exiting...")


# Using Python's version of casewhere from my C# experience
def menuOptions(choice):
    match choice:
        case "A":
            return "\nWelcome to login. Please provide your details."
        case "a":
            return "\nWelcome to login. Please provide your details."

        case "B":
            return "\nPlease enter details to register."
        case "b":
            return "\nPlease enter details to register."

        case "C":
            return "\nSaving and closing accounts file."
        case "c":
            return "\nSaving and closing accounts file."

        case "D":
            return "\nDisplay accounts: "
            # accountList = accounts.read()
            # return accountList
        case "d":
            return "\nDisplay accounts: "
            # accountList = accounts.read()
            # return accountList

        case "E":
            print("\nExiting...")
            # not runningProgram
            time.sleep(2)
            exit()
            return ""
        case "e":
            print("\nExiting...")
            # not runningProgram
            time.sleep(2)
            exit()
            return ""

        # If an exact match is not found, print "invalid" response and let user try again.
        case _:
            return "\nInvalid option. Please try again."


# while runningProgram:
while True:
    print("A) LOGIN")
    print("B) REGISTER")
    print("C) SAVE ACCOUNTS FILE")
    print("D) VIEW ACCOUNTS FILE")
    print("E) EXIT")
    menuChoice = input("Please select an option: ")
    result = menuOptions(str(menuChoice))
    print(result)
