def main():
    # Ejercicio 6
    lista = [1,2,3,4,5,6,7]

    ultimo = lista[-1]
    lista = [ultimo] + lista[:-1]

    for e in lista:
        print(e)

if __name__ == '__main__':
    main()
