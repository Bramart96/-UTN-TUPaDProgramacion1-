
# Ejercicio 4 - Escape Room

energia = 100
tiempo = 12
cerraduras = 0
alarma = False

while energia > 0 and tiempo > 0 and cerraduras < 3 and not alarma:
    print("Energia:", energia, "Tiempo:", tiempo)
    op = input("1 Forzar 2 Hackear 3 Descansar: ")

    if op == "1":
        energia -= 20
        tiempo -= 2
        cerraduras += 1
    elif op == "2":
        energia -= 10
        tiempo -= 3
        cerraduras += 1
    elif op == "3":
        energia = min(100, energia+15)
        tiempo -= 1

if cerraduras == 3:
    print("Victoria")
else:
    print("Derrota")
