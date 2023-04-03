# ////////////////////////////////////////////////////////////
# ALPHA VERSION of SimpleLogin
# PLEASE REFER TO simplelogin.py FOR ASSESSMENT!
# ////////////////////////////////////////////////////////////

import time

# existingAccounts = open("accounts.txt", "r")
# registerAccounts = open("accounts.txt", "a")
accounts = open("accounts.txt", "r")


def menuoptions(choice):
    # Using match, compare the passed value 'choice' against set values
    # If 'choice' matches a set value (e.g. "B"), start that specific function
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

        # If no match is found, print "invalid" response and let user try again.
        case _:
            return "\nInvalid option. Please try again.\n"


def login():
    # global existingAccounts
    # existingAccounts = open("accounts.txt", "r")
    global accounts
    accounts = open("accounts.txt", "r")
    print("\nWelcome to LOGIN. Please provide your existing details.")
    print("Or press ENTER (empty entry) to exit back to main menu.\n")
    username = str(input("USERNAME: "))
    if username == "":
        print("Empty entry received. Returning back to main menu...")
        return
    password = str(input("PASSWORD: "))
    if password == "":
        print("Empty entry received. Returning back to main menu...")
    combination = str(username + " " + password)
    # use combination to compare against entries in accounts.txt

    # check login information against accounts file
    # if login information matches:
    # print "login successful"
    # else
    # print "login failed, invalid details, try again"

    # print("Welcome back, " + username)

    # print("Invalid login details. Please try again")
    # login()


def register():
    # global registerAccounts
    # registerAccounts = open("accounts.txt", "a")
    global accounts
    accounts = open("accounts.txt", "r")
    print("\nWelcome to REGISTER. Please provide new details.\n")
    print("Or press ENTER now to exit back to main menu.")
    username = str(input("USERNAME: "))
    if username == "":
        print("Returning back to main menu...")
        return
    password = str(input("PASSWORD: "))
    registerAccounts.write("\n" + username + " " + password)
    print("Successfully registered! Welcome, " + username)
    return


def savefile():
    print("\nSaving...")
    # Close files is equivalent to saving them but must be opened again if user wants to login/register
    # registerAccounts.close()
    # existingAccounts.close()
    accounts.close()
    # Check to see if files have successfully closed
    # if registerAccounts.closed and existingAccounts.closed:
    #     print("File saved.")
    # else:
    #     print("Error encountered while saving. Please try again.")
    if accounts.closed:
        print("File saved.")
    else:
        print("Error encountered while saving. Please try again.")
    return


def displayaccounts():
    # accountList = existingAccounts.read()
    accountList = accounts.read()
    print("\n" + accountList)
    return


def exitprogram():
    # registerAccounts.close()
    # existingAccounts.close()
    accounts.close()
    print("\nExiting...")
    time.sleep(2)
    exit()
    return


# Menu interface:
while True:
    print("\nA) LOGIN")
    print("B) REGISTER")
    print("C) SAVE ACCOUNTS FILE")
    print("D) VIEW ACCOUNTS FILE")
    print("E) EXIT")
    menuChoice = input("Please select an option: ")
    result = menuoptions(str(menuChoice))
