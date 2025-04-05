salario = float(input("Ingrese el salario bruto: "))

renta = salario * 0.10
seguro = salario * 0.05
pension = salario * 0.03

descuentos = renta + seguro + pension
neto = salario - descuentos

print("Salario bruto: ", salario)
print("Descuentos: ", descuentos)
print("Salario neto: ", neto)
print("Salario neto: ",(salario_neto))