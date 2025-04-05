radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))
pi = 3.1416
area_base = pi * (radio * radio)
volumen_cilindro = area_base * altura
area_lateral = 2 * pi * radio * altura
area_superficial = area_lateral + (2 * area_base)

print("-------calculando--------")
print("-------------------------")
print("Radio ingresado: ", radio)
print("altura ingresada: ", altura)
print("el area superficial calculada es: ", area_superficial)

