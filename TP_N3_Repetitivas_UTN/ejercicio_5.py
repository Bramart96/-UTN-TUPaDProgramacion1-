
# Ejercicio 5 - Gladiador

nombre = input("Nombre: ")
while not nombre.isalpha():
    nombre = input("Error: ")

vida_j = 100
vida_e = 100
pociones = 3

while vida_j > 0 and vida_e > 0:
    print(nombre, vida_j, "Enemigo", vida_e)
    op = input("1 Ataque 2 Rafaga 3 Curar: ")

    if not op.isdigit():
        continue

    op = int(op)

    if op == 1:
        daño = 15
        if vida_e < 20:
            daño *= 1.5
        vida_e -= daño
    elif op == 2:
        for i in range(3):
            vida_e -= 5
    elif op == 3:
        if pociones > 0:
            vida_j += 30
            pociones -= 1

    vida_j -= 12

if vida_j > 0:
    print("Victoria")
else:
    print("Derrota")
