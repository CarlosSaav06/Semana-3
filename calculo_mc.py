peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))

altura_por_altura = altura * altura
imc = peso / altura_por_altura 
IMC = (imc * 100) // 1 / 100

print("-" * 60)
print("Peso ingresado: ", peso, "kg")
print("Altura ingresada: ", altura, "m")
print("IMC calculado: ", IMC)

print("Clasificación:", end=" ")
if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")

