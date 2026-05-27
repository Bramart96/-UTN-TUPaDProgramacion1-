def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))
print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(celsius))
