# Importing all libraries
import requests
import os
from cryptography.fernet import Fernet
from colorama import init
init(autoreset=True)
from colorama import Fore, Style

# Internet stuff
WebTimeout = 1

# Encryption setup
key = Fernet.generate_key()
with open('key.key', 'wb') as filekey:
   filekey.write(key)

# Main function
def flock():
    os.system('cls')
    input(f"Welcome to {Style.BRIGHT}Flock ALPHA{Style.DIM} (v0.1.0){Style.RESET_ALL+Fore.RED}\nWarning! Flock is currently under heavy development and features here may be changed or removed."+Style.RESET_ALL+"\n\nPress ENTER to continue")
    while True:
        os.system('cls')
        option = input(f"{Style.BRIGHT}Flock ALPHA{Style.DIM} (v0.1.0)\nEnter 'help' for full list of cmds{Style.RESET_ALL}\n\nflock> ")
        # Help command
        if option == 'help':
            input(f"{Fore.LIGHTBLUE_EX}\nEncryption and Decryption\nencrypt - Encrypts a given file\ndecryption - Decrypt the given file\n\n{Style.RESET_ALL+Fore.LIGHTMAGENTA_EX}Internet\nPing - Checks if a webpage responds back {Style.RESET_ALL}Press ENTER to quit viewing")
        elif option == 'encrypt':
            filename = input(f"{Fore.RED}Make sure the file is in the same folder as main.py and enter the full file name like text.txt{Style.RESET_ALL}\n\nEnter the file: ")
            with open('key.key', 'rb') as key:
                key = key.read()
                fernet = Fernet(key)
            with open(filename, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
        # Decrypt command        
        elif option == 'decrypt':
            filename = input(f"{Fore.RED}Make sure the file is in the same folder as main.py and enter the full file name like text.txt{Style.RESET_ALL}\n\nEnter the file: ")
            with open(filename, 'rb') as enc_file:
                encrypted = enc_file.read()
            decrypted = fernet.decrypt(encrypted)
            with open(filename, 'wb') as dec_file:
                dec_file.write(decrypted)
        # Ping command
        elif option == 'ping':
            website = input('Enter a FULL website link for example, http://www.google.com\n')
            try:
                requests.head(website, timeout=WebTimeout)
                input('\nThe internet connection is active!. Press ENTER to dismiss')
            except requests.ConnectionError:
                input("\nThe internet connection is down or server did not respond. Press ENTER to dismiss")
            except requests.exceptions.MissingSchema:
                input("\nMake sure to include the 'http://' next time. Press ENTER to dismiss")  
        else:
            input('\nYou entered a invalid command. To see all commands, please check the help command. Remember that commands are case sensitive. Press ENTER to reset.')
        
flock()