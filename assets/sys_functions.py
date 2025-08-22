## IMPORTS ##
import os
import time



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


# Function to get user choice
def choice(index):
    def invalid_choice():
        clear()
        print("Invalid choice!")
        time.sleep(1.5)
        clear()
    while True:
        try:
            scelta = int(input("\nPlease enter the number of your choice: "))
            if scelta in range(1, index + 1):
                return scelta
            else:
                invalid_choice()
        
        except ValueError:
            invalid_choice()
