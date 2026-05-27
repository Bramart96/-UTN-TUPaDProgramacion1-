"""
Ejercicio 8
Gestión simple de stock de productos.
"""

# Este bloque crea un diccionario inicial con productos y stock
stock = {"Arroz": 10, "Fideos": 8, "Azúcar": 15}

producto = input("Ingresá el producto a consultar: ")

# Este bloque consulta si el producto existe y permite actualizar o crear stock
if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    unidades = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += unidades
else:
    unidades = int(input("Producto nuevo. Ingresá stock inicial: "))
    stock[producto] = unidades

print("Stock actualizado:", stock)
