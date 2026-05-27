"""
Ejercicio 10
Invertir claves y valores de un diccionario.
"""

# Este bloque define un diccionario con países como clave y capitales como valor
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

# Este bloque invierte el diccionario usando comprensión: capital -> país
capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario invertido:")
print(capitales)
