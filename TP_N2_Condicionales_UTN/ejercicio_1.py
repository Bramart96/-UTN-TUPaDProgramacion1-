hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes in [1,2] or (mes == 3 and dia < 21):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or mes in [4,5] or (mes == 6 and dia < 21):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or mes in [7,8] or (mes == 9 and dia < 21):
        print("Verano")
    else:
        print("Otoño")
else:
    if (mes == 12 and dia >= 21) or mes in [1,2] or (mes == 3 and dia < 21):
        print("Verano")
    elif (mes == 3 and dia >= 21) or mes in [4,5] or (mes == 6 and dia < 21):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or mes in [7,8] or (mes == 9 and dia < 21):
        print("Invierno")
    else:
        print("Primavera")
