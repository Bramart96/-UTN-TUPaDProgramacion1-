def main():
    # Ejercicio 4
    lista = [1,2,2,3,4,4,5,6,6]

    sin_repetidos = []

    for elem in lista:
        if elem not in sin_repetidos:
            sin_repetidos.append(elem)

    for e in sin_repetidos:
        print(e)

if __name__ == '__main__':
    main()
