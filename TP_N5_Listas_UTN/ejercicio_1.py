def main():
    # Ejercicio 1
    notas = [7, 8, 6, 9, 10, 5, 7, 8, 6, 9]

    # Mostrar lista
    for nota in notas:
        print(nota)

    # Promedio
    promedio = sum(notas) / len(notas)
    print("Promedio:", promedio)

    # Mayor y menor
    print("Nota más alta:", max(notas))
    print("Nota más baja:", min(notas))

if __name__ == '__main__':
    main()
