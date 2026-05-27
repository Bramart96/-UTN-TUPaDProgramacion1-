def main():
    # Ejercicio 7
    temps = [
        [10,20],[12,22],[8,18],[9,19],[11,21],[7,17],[6,16]
    ]

    minimas = [t[0] for t in temps]
    maximas = [t[1] for t in temps]

    print("Promedio mínimas:", sum(minimas)/len(minimas))
    print("Promedio máximas:", sum(maximas)/len(maximas))

    amplitudes = [t[1]-t[0] for t in temps]
    print("Mayor amplitud en día:", amplitudes.index(max(amplitudes))+1)

if __name__ == '__main__':
    main()
