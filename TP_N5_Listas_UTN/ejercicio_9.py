# Nota: Se agregan comentarios para explicar la lógica de manejo de matrices (listas de listas).
def get_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingrese un número válido.")

def main():
    # Ejercicio 9
    tablero = [["-" for _ in range(3)] for _ in range(3)]

    for turno in range(9):
        jugador = "X" if turno % 2 == 0 else "O"
        fila = get_int("Fila (0-2): ")
        col = get_int("Columna (0-2): ")

        if tablero[fila][col] == "-":
            tablero[fila][col] = jugador

        for fila in tablero:
            print(fila)

if __name__ == '__main__':
    main()
