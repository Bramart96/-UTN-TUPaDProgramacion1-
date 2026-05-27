def get_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingrese un número válido.")

def main():
    # Ejercicio 11
    estudiantes = ["Ana","Juan","Luis","Sofia","Pedro","Maria","Lucas","Elena","Mateo","Carla"]

    nombre = input("Buscar nombre: ")

    if nombre in estudiantes:
        print("Está en la lista en posición:", estudiantes.index(nombre))
    else:
        print("No está en la lista")

if __name__ == '__main__':
    main()
