"""
Ejercicio 6
Registrar alumnos y calcular promedio.
"""

# Este bloque guarda nombres de alumnos como clave y una tupla de 3 notas como valor
alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = (
        float(input("Nota 1: ")),
        float(input("Nota 2: ")),
        float(input("Nota 3: "))
    )
    alumnos[nombre] = notas

# Este bloque recorre el diccionario y calcula el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")
