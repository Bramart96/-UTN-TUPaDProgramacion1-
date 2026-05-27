def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print("Horas equivalentes:", segundos_a_horas(segundos))
