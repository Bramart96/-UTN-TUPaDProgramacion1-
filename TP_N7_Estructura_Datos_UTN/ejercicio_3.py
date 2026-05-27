"""
Ejercicio 3
Generar una lista con solo los nombres de las frutas.
"""

# Este bloque usa .keys() para extraer solo las claves del diccionario y convertirlas en lista
precios_frutas = {
    'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450,
    'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300
}

frutas = list(precios_frutas.keys())

print("Lista de frutas:")
print(frutas)
