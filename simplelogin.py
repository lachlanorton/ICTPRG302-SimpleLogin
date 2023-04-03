# /////////////////////////////////////////////////////////////
# SimpleLogin program
# For ICTPRG302 Assessment Event 2 - Project
#
# Author: Lachlan Orton
# Start Date: 15/03/2023
# Last Updated: 28/03/2023
# On GitHub?: Yes
# TAFE NSW St. Leonard's / ICTPRG302 Programming and Data
#
# This program handles logging users into accounts if their
# details are present. It also handles registering new users
# and adding those details to file, alongside other functions.
# /////////////////////////////////////////////////////////////

import time
import random
import string

allAccounts = open("accounts.txt", "r")


# This function handles interpreting what choice was made at menu screen, and what to do from that choice.
def menuoptions(choice):
    # Using match, compare the parameter 'choice' against set values
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
            print("\nInvalid response. Please try again.")
            return "\n"


# This function handles logging user in by comparing against records in accounts file.
def login():
    # Ensure file is open in read mode.
    global allAccounts
    allAccounts = open("accounts.txt", "r")
    # Visual message for user, welcome to the login screen.
    print("\nWelcome to LOGIN. Please provide your existing details.")
    print("Or press ENTER (empty entry) to exit back to main menu.\n")
    # Ask user for USERNAME.
    username = str(input("USERNAME: "))
    # If USERNAME input is empty, send user back to main menu after delay.
    if username == "":
        print("Empty entry received. Returning back to main menu...")
        time.sleep(2)
        return
    while True:
        # Ask user for PASSWORD
        password = str(input("PASSWORD: "))
        # If PASSWORD is empty, alert user and get them to try again.
        # Otherwise, accept PASSWORD entry and break out of while loop.
        if password == "":
            print("Password can't be empty! Try again...")
        else:
            break

    # 'combination' will be used to compare against records inside accounts file.
    # Since accounts file has a standardised format (username password), we can create
    # the combination variable with this standard.
    combination = str(username + " " + password)
    # 'account' variable stores each individual line within accounts file.
    account = allAccounts.readlines()

    checkAccount = ""
    # Using for loop, we go through each line, strip the line to it's pure string, and compare to 'combination'
    for entry in account:
        checkAccount = entry.strip()
        # If current line in file matches our combination, account exists, therefore login success!
        if checkAccount == combination:
            print("Successfully logged in. Welcome back, " + username)
            time.sleep(2)
            break
    # If no lines match our combination, account does not exist or invalid details provided.
    # Return user to main menu.
    if checkAccount != combination:
        print("\nInvalid details provided. Log in failed.")
        print("Returning to main menu...")
        time.sleep(2)


# This function handles writing new user details to accounts file.
def register():
    global allAccounts
    allAccounts = open("accounts.txt", "a")
    print("\nWelcome to REGISTER. Please provide new details.")
    print("Or press ENTER (empty entry) to exit back to main menu.\n")
    # Ask user for USERNAME.
    username = str(input("USERNAME: "))
    # If USERNAME input is empty, send user back to main menu after delay.
    if username == "":
        print("Empty entry received. Returning back to main menu...")
        time.sleep(2)
        return
    # Give user password options (user defined vs randomly generated)
    print("\nA) I want to make my own password")
    print("B) I want a randomly generated password")
    while True:
        # Ask user for password choice.
        passwordPref = str(input("Please choose your preference for password: "))
        # If user chooses A/a, allow user to define their own password.
        if passwordPref == "A" or passwordPref == "a":
            print("\nYou have chosen to make your own password.")
            print("Please note that the password length must be between 6-20 characters long.")
            while True:
                # Ask user for PASSWORD
                password = str(input("PASSWORD: "))
                # Grab length of password and add to variable to use for comparison
                passwordLen = len(password)
                # If password is empty, send back.
                if password == "":
                    print("Password can't be empty! Try again...")
                # If password is less than 6 characters long, send back.
                if passwordLen < 6:
                    print("Password is less than 6 characters long! Try again...")
                # If password is more than 20 characters long, send back.
                if passwordLen > 20:
                    print("Password is longer than 20 characters long! Try again...")
                # If password matches restrictions, leave while loop and continue.
                elif 6 <= passwordLen <= 20:
                    break
            break
        # If user chooses B/b, generate random password.
        elif passwordPref == "B" or passwordPref == "b":
            print("\nYou have chosen a randomly generated password.")
            # Set 'password' variable to value returned from randompassword() function
            password = randompassword()
            print("\nYour password is: " + password)
            break
        print("\nInvalid response. Please try again.\n")

    # Append new username and password to file on new line according to standard
    allAccounts.write("\n" + username + " " + password)
    print("Success! \nPlease note your new username and password details down.\n")
    time.sleep(4)
    print("Successfully registered! Welcome, " + username)
    time.sleep(2)
    return


# This function handles creating a random password for the user.
def randompassword():
    # Ask user for password length (in characters).
    while True:
        askLength = input("How long (in characters) would you like your password to be? (E.g. 6): ")
        # Check if input isn't empty
        if askLength:
            # Cast input value to integer and place in new variable
            passLength = int(askLength)
            # Check if password is less than 6 characters long
            if passLength < 6:
                print("Password is less than 6 characters long! Try again...")
            # Check if password is more than 20 characters long
            if passLength > 20:
                print("Password is longer than 20 characters long! Try again...")
            # If password fits restrictions, exit while loop.
            elif 6 <= passLength <= 20:
                break
        else:
            print("Password length cannot be empty! Try again...")
    # Present user with preferences they can choose for password generation.
    print("\nPlease choose what you would like your password to be made of.")
    print("A) Letters\nB) Numbers\nC) Special characters\nENTER) I've completed my choices, make my password!")

    # Define string pool for character sets to be placed in
    # Password generation will grab random characters from this pool
    passChoices = ""
    while True:
        # Ask user for their preferences for password generation.
        passPref = str(input("\nPlease input your preferences: "))
        if passPref == "A" or passPref == "a":
            # Adds letters (lowercase and uppercase) to pool
            passChoices += string.ascii_letters
            print("Letters added to your password preference.")
        elif passPref == "B" or passPref == "b":
            # Adds numbers to pool
            passChoices += string.digits
            print("Numbers added to your password preference.")
        elif passPref == "C" or passPref == "c":
            # Adds special characters to pool
            passChoices += string.punctuation
            print("Special characters added to your password preference.")
        elif passPref == "":
            # If user attempts to complete preferences without choosing any, alert them and restart.
            if passChoices == "":
                print("You have not made any preferences yet!")
            else:
                print("Password preferences completed.")
                time.sleep(2)
                break
        else:
            print("Invalid response. Please try again.")

    # Create a blank string for our randomly generated password.
    ranPass = ""
    # Using for loop, choose a random character from our pool of preferences and add to ranPass string.
    # For loop only runs as many times as the password length was input as.
    for i in range(passLength):
        passChar = random.choice(passChoices)
        ranPass += passChar
    # Send randomly generated password back to register() function.
    return ranPass


# This function handles saving the working file 'accounts'.
def savefile():
    print("\nSaving...")
    # Close file is equivalent to saving them but must be opened again if user wants to login/register
    allAccounts.close()
    # Check to see if file has successfully closed
    if allAccounts.closed:
        print("File saved.")
    else:
        print("Error encountered while saving. Please try again.")
    return


# This function handles displaying the contents of accounts file.
def displayaccounts():
    # Ensure file is open in read mode.
    global allAccounts
    allAccounts = open("accounts.txt", "r")
    # Read file and add to variable accountList.
    accountList = allAccounts.read()
    # Print accountList variable
    print("\n" + accountList)
    return


# This function handles terminating the executable.
def exitprogram():
    # Ensure file is closed and saved
    allAccounts.close()
    # Print visual message for user
    print("\nExiting...")
    # Delay and then terminate executable
    time.sleep(2)
    exit()
    return


# Menu interface.
# While loop allows for menu choices to return for user once function is completed or broken out of.
while True:
    # Print available menu choices.
    print('''
############ MENU ############
A) LOGIN                  
B) REGISTER
C) SAVE ACCOUNTS FILE
D) VIEW ACCOUNTS FILE
E) EXIT
##############################''')
    # Ask user for input of menu choice.
    menuChoice = input("Please select an option: ")
    # Start menuoptions() function with menuChoice as parameter.
    result = menuoptions(str(menuChoice))
