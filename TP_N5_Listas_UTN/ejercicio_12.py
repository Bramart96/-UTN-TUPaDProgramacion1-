def get_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingrese un número válido.")

def main():
    # Ejercicio 12
    numeros = []

    for i in range(8):
        numeros.append(get_int("Ingrese número: "))

    print("Original:", numeros)
    print("Ordenada:", sorted(numeros))
    print("Descendente:", sorted(numeros, reverse=True))

if __name__ == '__main__':
    main()
