## IMPORTS ##
from Crypto.PublicKey import RSA, ElGamal
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from Crypto.Random import random
import base64
import string



## ALGORITHM FUNCTIONS ##

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " "
# Encryption function
def encrypt(message, key, method):
    if method == "Custom":
        full_pass = (key[::-1] * (len(message) // len(key) + 1))[:len(message)]
        cripted_message_listed = []

        for i, (char, p) in enumerate(zip(message, full_pass)):
            char_pos = alphabet.index(char)
            pass_pos = alphabet.index(p)
            if i < len(message) // 2:
                new_pos = (char_pos + pass_pos) % len(alphabet)
            else:
                new_pos = (char_pos - pass_pos) % len(alphabet)
            cripted_message_listed.append(alphabet[new_pos])

        return ''.join(cripted_message_listed)[::-1]


# Decryption function
def decrypt(message, key, method):
    if method == "Custom":
        message = message[::-1]
        full_pass = (key[::-1] * (len(message) // len(key) + 1))[:len(message)]
        decripted_message_listed = []

        for i, (char, p) in enumerate(zip(message, full_pass)):
            char_pos = alphabet.index(char)
            pass_pos = alphabet.index(p)
            if i < len(message) // 2:
                new_pos = (char_pos - pass_pos) % len(alphabet)
            else:
                new_pos = (char_pos + pass_pos) % len(alphabet)
            decripted_message_listed.append(alphabet[new_pos])

        return ''.join(decripted_message_listed)
