def get_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingrese un número válido.")

def main():
    # Ejercicio 5
    estudiantes = ["Ana","Juan","Luis","Sofia","Pedro","Maria","Lucas","Elena"]

    accion = input("¿Agregar o eliminar?: ")

    if accion == "agregar":
        nuevo = input("Nombre: ")
        estudiantes.append(nuevo)
    elif accion == "eliminar":
        elim = input("Nombre: ")
        if elim in estudiantes:
            estudiantes.remove(elim)

    for e in estudiantes:
        print(e)

if __name__ == '__main__':
    main()
