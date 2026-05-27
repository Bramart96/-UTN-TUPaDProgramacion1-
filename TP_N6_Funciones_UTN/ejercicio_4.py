import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))

print("Área:", round(calcular_area_circulo(radio), 2))
print("Perímetro:", round(calcular_perimetro_circulo(radio), 2))
