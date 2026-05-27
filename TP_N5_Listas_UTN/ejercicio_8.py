def main():
    # Ejercicio 8
    notas = [
        [7,8,9],
        [6,7,8],
        [9,9,10],
        [5,6,7],
        [8,8,8]
    ]

    # Promedio por estudiante
    for i in range(len(notas)):
        print("Promedio estudiante", i+1, ":", sum(notas[i])/len(notas[i]))

    # Promedio por materia
    for j in range(3):
        suma = 0
        for i in range(5):
            suma += notas[i][j]
        print("Promedio materia", j+1, ":", suma/5)

if __name__ == '__main__':
    main()
