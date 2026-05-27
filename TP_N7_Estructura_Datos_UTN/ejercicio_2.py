"""
Ejercicio 2
Actualizar precios existentes dentro del diccionario.
"""

# Este bloque parte del diccionario ya ampliado y modifica precios existentes
precios_frutas = {
    'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450,
    'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300
}

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print("Precios actualizados:")
print(precios_frutas)
