# Importing all libraries
from fileinput import filename
import os
from cryptography.fernet import Fernet
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style

# Encryption setup
key = Fernet.generate_key()
with open('key.key', 'wb') as filekey:
   filekey.write(key)

# Main function
def flock():
    os.system('cls')
    input("Welcome to "+Style.BRIGHT+"Flock ALPHA"+Style.DIM+" (v0.1.0)"+Style.RESET_ALL+Fore.RED+"\nWarning! Flock is currently under heavy development and features here may be changed or removed."+Style.RESET_ALL+"\n\nPress ENTER to continue")
    while True:
        os.system('cls')
        option = input(Style.BRIGHT+"Flock ALPHA"+Style.DIM+" (v0.1.0)\nEnter 'help' for full list of cmds"+Style.RESET_ALL+"\n\nflock> ")
        if option == 'help':
            input("Encryption and Decryption\n encrypt - Encrypts a given file\ndecryption - Decrypt the given file\n\nPress ENTER to quit viewing")
        elif option == 'encrypt':
            filename = input(Fore.RED+"Make sure the file is in the same folder as main.py and enter the full file name like text.txt"+Style.RESET_ALL+"\nEnter the file: ")
            with open('key.key', 'rb') as key:
                key = key.read()
                fernet = Fernet(key)
            with open(filename, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
        elif option == 'decrypt':
            filename = input(Fore.RED+"Make sure the file is in the same folder as main.py and enter the full file name like text.txt"+Style.RESET_ALL+"\nEnter the file: ")
            with open(filename, 'rb') as enc_file:
                encrypted = enc_file.read()
            decrypted = fernet.decrypt(encrypted)
            with open(filename, 'wb') as dec_file:
                dec_file.write(decrypted)

flock()
