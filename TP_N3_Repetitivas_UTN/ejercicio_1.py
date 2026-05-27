
# Ejercicio 1 - Caja del Kiosco

nombre = input("Ingrese nombre: ")
while not nombre.isalpha():
    nombre = input("Error. Ingrese nombre válido: ")

cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Error. Ingrese número válido mayor a 0: ")

cantidad = int(cantidad)

total_sin = 0
total_con = 0

for i in range(1, cantidad+1):
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit():
        precio = input("Error. Ingrese precio válido: ")
    precio = int(precio)

    desc = input("¿Descuento? (S/N): ").lower()
    while desc not in ["s","n"]:
        desc = input("Error. Ingrese S o N: ").lower()

    total_sin += precio

    if desc == "s":
        precio = precio * 0.9

    total_con += precio

ahorro = total_sin - total_con
promedio = total_con / cantidad

print("Total sin descuentos:", total_sin)
print(f"Total con descuentos: {total_con:.2f}")
print(f"Ahorro: {ahorro:.2f}")
print(f"Promedio: {promedio:.2f}")
