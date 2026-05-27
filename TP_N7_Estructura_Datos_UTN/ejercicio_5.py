"""
Ejercicio 5
Analizar palabras únicas y frecuencia de una frase.
"""

# Este bloque solicita una frase, la separa en palabras y normaliza a minúsculas
frase = input("Ingresá una frase: ").lower().split()

# Este bloque crea un set para obtener palabras únicas sin repetir
palabras_unicas = set(frase)

# Este bloque cuenta cuántas veces aparece cada palabra usando un diccionario
frecuencia = {}
for palabra in frase:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia de palabras:", frecuencia)
