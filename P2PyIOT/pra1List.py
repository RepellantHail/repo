import sys

def main():
    clearConsole()
    print("\033[32m\t\033[1mPrimera practica\033[37m\033[0m") #White font
    #numeros = [0,1,2,3,4,5,6,7,8,9]

    numeros = []
    while True:#Capturar Numeros
        try:
            num = int(input("Ingrese un Numero: \n"))
            numeros.append(num)
            clearConsole()
        except ValueError:
            break

    print("\033[31mLista: \t\t\t\t \033[31m", numeros)

    #imprimir sublista 2 elementos mitad de lista    
    print("\033[37mMitad de la lista: \t\t \033[34m", numeros[len(numeros) // 2 - 1 : len(numeros) // 2 + 1])
    #Imprimir primer y ultimo elemento de la lista
    print("\033[37mPrimer y Ultimo Elemento: \t \033[34m", numeros[0], numeros[-1])    
    #Agregar elementos al final de la misma
    numeros.extend(numeros)
    print("\033[37mLista agregada: \t\t \033[34m", numeros)
    #Ordenar elementos de la lista
    numeros.sort()
    print("\033[37mLista Ordenada: \t\t \033[34m", numeros)
    #Ordenar elementos de la lista de mayor a menor
    numeros.sort(reverse=True)
    print("\033[37mLista Ordenada Inversa: \t \033[34m", numeros)
    #Cubo de elementos
    print("\033[37mCubo de elementos: \t\t \033[34m", list(map(lambda e: e ** 3, numeros)))

def clearConsole():
    #Clear Screen
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()

main()