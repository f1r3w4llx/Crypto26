## IMPORTS ##
from sys_functions import *
from algorithms import encrypt, decrypt


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
        print("\nDo you want to go back to the main menu? (1) Yes (2) No")
        return True if choice(2) == 1 else quit_program()



## ALGORITHMS MENUS ##

# Symmetric encryption methods menu
def symmetric_encrypt_menu(method):
    clear()
    banner_print()
    print(f"You have chosen the {method} encryption method.")
    message, key = get_input("message"), get_input("password")
    print(f"\nEncryption completed successfully! Your encrypted message is: [+]  {encrypt(message, key, method)}  [+]!")
    return quit_menù()


# Symmetric decryption methods menu
def symmetric_decrypt_menu(method):
    clear()
    banner_print()
    print(f"You have chosen the {method} decryption method.")
    message, key = get_input("message"), get_input("password")
    print(f"\nDecryption completed successfully! Your decrypted message is: [+]  {decrypt(message, key, method)}  [+]!")
    return quit_menù()
