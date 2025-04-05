dolares = float(input("Ingrese la cantidad en dolares: "))

tasa_euros = 0.92
tasa_libras = 0.82
tasa_yenes = 134.50

euros = dolares * tasa_euros
libras = dolares * tasa_libras
yenes = dolares * tasa_yenes

print("-" * 60)
print("Cantidad en dolares: ", dolares)
print("La cantidad equivalente en euros es: ", euros)
print("La cantidad equivalente en libras: ", libras)
print("La cantidad equivalente en yenes es: ", yenes)

