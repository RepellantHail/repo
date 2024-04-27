import sys
import re

def is_valid_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Use the re.match() function to check if the email matches the pattern
    return True if re.match(pattern, email) else False

def main():
    white = "\033[37m"
    blue  = "\033[34m"
    red   = "\033[31m"

    clearConsole()
    print("\033[32m\t\033[1mTercera practica\033[37m\033[0m") #Print title
    # email = input("Ingrese una dirección de correo electrónico: ")
    email = "luismodesto@gmail.com"
    print( red + "Dirección \t", email)
    ans = "es válida" if is_valid_email(email) else "no es válida"
    print(white +"La dirección \t"+ blue, ans)

def clearConsole():
    #Clear Screen
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()

main()