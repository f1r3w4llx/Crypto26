## IMPORTS ##
import os
import time
from algorithms import RSA, ElGamal, PKCS1_OAEP, Random, random



## SYSTEM FUNCTIONS ##

# Clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Print the banner
banner = r"""
#-----------------------------------------------------------------------------#
..######..########..##....##.########..########..#######...#######...#######.
.##....##.##.....##..##..##..##.....##....##....##.....##.##.....##.##.....##
.##.......##.....##...####...##.....##....##....##.....##........##.##.......
.##.......########.....##....########.....##....##.....##..#######..########.
.##.......##...##......##....##...........##....##.....##.##........##.....##
.##....##.##....##.....##....##...........##....##.....##.##........##.....##
..######..##.....##....##....##...........##.....#######..#########..#######.
#-----------------------------------------------------------------------------#
"""

def banner_print():
    print(f"\033[35m{banner}\033[0m")



## PROGRAM FUNCTIONS ##

# Function to quit the program
def quit_program():
    print("\nThanks for using Crypto26!\n")
    time.sleep(1)
    exit()


# Function to get user choice
def choice(index):
    def invalid_choice():
        print("\nInvalid choice!")
        time.sleep(1.5)
    while True:
        try:
            scelta = int(input("\nPlease enter the number of your choice: "))
            if 1 <= scelta <= index:
                return scelta
            else:
                invalid_choice()
        except ValueError:
            invalid_choice()


# Function to get password & message input + RSA keys
def get_input(type):
    def check(user_input):
        if user_input == "":
            print(f"\nThe {type} cannot be empty!")
            time.sleep(1.5)
        else:
            return True

    while True:
        if type == "password":
            user_input = input("Please enter your password, all the symbols are allowed: ")
            if check(user_input):
                return user_input
        elif type == "message":
            user_input = input("\nPlease enter your message, all the symbols are allowed: ")
            if check(user_input):
                return user_input
