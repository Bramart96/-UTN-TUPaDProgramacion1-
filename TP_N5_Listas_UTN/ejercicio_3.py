def main():
    # Ejercicio 3
    import random

    numeros = [random.randint(1,100) for _ in range(15)]

    pares = []
    impares = []

    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    print("Pares:", len(pares))
    print("Impares:", len(impares))

if __name__ == '__main__':
    main()
