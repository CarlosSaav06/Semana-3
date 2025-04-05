precio = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento aplicado"))
descuento = (precio * porcentaje_descuento) / 100
precio_con_descuento = precio - descuento

porcentaje_iva = float(input("Ingrese el porcentaje de iva: "))
iva = (precio_con_descuento * porcentaje_iva) / 100
precio_final = (precio_con_descuento + iva)

print("------calculando------")
print("precio original: ", precio)
print("Descuento aplicado: ", descuento)
print("Precio con descuento:", precio_con_descuento)
print("IVA calculado:", iva)
print("Precio final:", precio_final)