## IMPORTS ##
from .sys_functions import clear, banner_print, choice



## MENUS ##

# Main menu
def main_menu():
    clear()
    banner_print()
    print("\nWelcome to the main menu, please choose an option:\n")
    print("1. Encrypt a message\n2. Decrypt a message\n5. Exit")
    return choice(3)

# Submenu for encryption methods
def encrypt_menu():
    clear()
    banner_print()
    print("\nChoose an encryption method:\n")
    print("1. Symmetric - Custom!\n2. Symmetric - AES\n3. Symmetric - DES\n4. Symmetric - 3DES\n5. Asymmetric - RSA\n6. Asymmetric - ElGamal\n7. Back to main menu")
    return choice(7)

# Submenu for decryption methods
def decrypt_menu():
    clear()
    banner_print()
    print("\nChoose a decryption method:\n")
    print("1. Symmetric - Custom!\n2. Symmetric - AES\n3. Symmetric - DES\n4. Symmetric - 3DES\n5. Asymmetric - RSA\n6. Asymmetric - ElGamal\n7. Back to main menu")
    return choice(7)

# Quit menu
def quit_menù():
    while True:
        clear()
        banner_print()
        print("\n\nDo you want to go back to the main menu?\n")
        print("1. Yes\n2. No")
        return choice(2)