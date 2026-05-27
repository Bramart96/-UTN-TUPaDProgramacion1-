def main():
    # Ejercicio 13
    puntajes = [450, 1200, 875, 990, 300, 1500, 640]

    print("Mayor:", max(puntajes))
    print("Menor:", min(puntajes))

    ranking = sorted(puntajes, reverse=True)
    print("Ranking:", ranking)

    print("Posición de 990:", ranking.index(990)+1)

if __name__ == '__main__':
    main()
