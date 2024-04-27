import sys

def main():
    white = "\033[37m"
    blue  = "\033[34m"
    red  = "\033[31m"

    clearConsole()
    print("\033[32m\t\t\033[1mSegunda practica\033[37m\033[0m") #Print title
    cadena = input("Ingrese Cadena de Texto\n")
    # cadena = "Cadena de texto para pruebas de la practica"
    print(red + "Cadena: \t\t\t" + red, cadena)
    print(blue + "1. ¿Primera letra mayúscula?: \t"     + white, checker         (cadena))
    print(blue + "2. Número de Palabras:  \t"           + white, wordCounter     (cadena))
    print(blue + "3. Lista de Palabras:  \t\t"          + white, cadenaALista    (cadena))
    print(blue + "4. Cadena Invertida:  \t\t"           + white, cadenaInvertida (cadena))
    print(blue + "5. Última letra en mayúscula:  \t"    + white, palabraMayuscula(cadena))
    
def checker(cadena):
    # Devuelve verdadero o falso si la primera letra de la cadena es mayúscula
    return cadena[0].isupper()
    
def wordCounter(cadena):
    # Cuenta las palabras que forman la cadena de texto
    return len(cadena.split())
    
def cadenaALista(cadena):
    # Regresa una lista con las palabras que forman la cadena de texto
    return cadena.split()
    
def cadenaInvertida(cadena):
    # Regresa la cadena de texto invertida
    words = cadena.split()
    words.reverse()
    return " ".join(words)
    
def palabraMayuscula(cadena):
    # Imprime la cadena original con la última letra de cada palabra en mayúscula
    words = cadena.split()
    modified_words = []
    for word in words:
        modified_word = word[:-1] + word[-1].upper()
        modified_words.append(modified_word)
    return " ".join(modified_words)

def clearConsole():
    #Clear Screen
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()

main()