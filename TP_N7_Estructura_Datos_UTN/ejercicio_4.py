"""
Ejercicio 4
Agenda telefónica con 5 contactos.
"""

# Este bloque carga contactos en un diccionario usando nombre como clave y teléfono como valor
contactos = {}

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    telefono = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = telefono

# Este bloque consulta un nombre y verifica si existe en el diccionario
buscar = input("Ingresá un nombre para buscar su número: ")

if buscar in contactos:
    print(f"El número de {buscar} es {contactos[buscar]}")
else:
    print("Contacto no encontrado.")
