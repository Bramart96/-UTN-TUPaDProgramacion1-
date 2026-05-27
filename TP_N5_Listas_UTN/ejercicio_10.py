def main():
    # Ejercicio 10
    ventas = [
        [10,20,30,40,50,60,70],
        [5,15,25,35,45,55,65],
        [8,18,28,38,48,58,68],
        [12,22,32,42,52,62,72]
    ]

    # Total por producto
    for i in range(4):
        print("Producto", i+1, ":", sum(ventas[i]))

    # Día con más ventas
    totales_dias = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
    print("Día con más ventas:", totales_dias.index(max(totales_dias))+1)

    # Producto más vendido
    totales_productos = [sum(p) for p in ventas]
    print("Producto más vendido:", totales_productos.index(max(totales_productos))+1)

if __name__ == '__main__':
    main()
