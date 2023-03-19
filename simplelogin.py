# ///////////////////////////////////////////////////////////
# SimpleLogin program
# For ICTPRG302 Assessment Event 2 - Project
#
# Author: Lachlan Orton
# Start Date: 15/03/2023
# Last Updated: 19/03/2023
# On GitHub?: Yes
# TAFE NSW St. Leonard's / ICTPRG302 Programming and Data
# ///////////////////////////////////////////////////////////

import time

# global existingAccounts
# global registerAccounts
existingAccounts = open("accounts.txt", "r")
registerAccounts = open("accounts.txt", "a")


def menuoptions(choice):
    match choice:
        case "A":
            login()
            return "\n"
        case "a":
            login()
            return "\n"

        case "B":
            register()
            return "\n"
        case "b":
            register()
            return "\n"

        case "C":
            savefile()
            return "\n"
        case "c":
            savefile()
            return "\n"

        case "D":
            displayaccounts()
            return "\n"
        case "d":
            displayaccounts()
            return "\n"

        case "E":
            exitprogram()
            return "\n"
        case "e":
            exitprogram()
            return "\n"

        # If an exact match is not found, print "invalid" response and let user try again.
        case _:
            return "\nInvalid option. Please try again.\n"


def login():
    # existingAccounts = open("accounts.txt", "r")
    print("\nWelcome to LOGIN. Please provide your existing details.\n")
    print("Or press ENTER now to exit back to main menu.")
    username = str(input("USERNAME: "))
    if username == "":
        print("Returning back to main menu...")
        return ""
    password = str(input("PASSWORD: "))

    # check login information against accounts file
    # if login information matches:
    # print "login successful"
    # else
    # print "login failed, invalid details, try again"

    # print("Welcome back, " + username)

    # print("Invalid login details. Please try again")
    # login()


def register():
    # registerAccounts = open("accounts.txt", "a")
    print("\nWelcome to REGISTER. Please provide new details.\n")
    print("Or press ENTER now to exit back to main menu.")
    username = str(input("USERNAME: "))
    if username == "":
        print("Returning back to main menu...")
        return ""
    password = str(input("PASSWORD: "))
    registerAccounts.write("\n" + username + " " + password)
    print("Successfully registered! Welcome, " + username)
    return ""


def savefile():
    registerAccounts.close()
    print("File saved.")
    # problem - once file is closed, can't complete further actions like login/register/view
    # how to re-open file once it has been "saved" (closed)
    return ""


def displayaccounts():
    accountList = existingAccounts.read()
    print("\n" + accountList)
    return ""


def exitprogram():
    print("\nExiting...")
    time.sleep(2)
    exit()
    return ""


# Menu interface:
while True:
    print("A) LOGIN")
    print("B) REGISTER")
    print("C) SAVE ACCOUNTS FILE")
    print("D) VIEW ACCOUNTS FILE")
    print("E) EXIT")
    menuChoice = input("Please select an option: ")
    result = menuoptions(str(menuChoice))
