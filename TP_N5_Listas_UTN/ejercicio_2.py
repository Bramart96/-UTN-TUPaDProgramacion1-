def get_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingrese un número válido.")

def main():
    # Ejercicio 2
    productos = []

    for i in range(5):
        prod = input("Ingrese producto: ")
        productos.append(prod)

    # Ordenar
    ordenados = sorted(productos)
    print("Lista ordenada:")
    for p in ordenados:
        print(p)

    # Eliminar producto
    elim = input("¿Qué producto desea eliminar?: ")
    if elim in productos:
        productos.remove(elim)

    print("Lista actualizada:")
    for p in productos:
        print(p)

if __name__ == '__main__':
    main()
