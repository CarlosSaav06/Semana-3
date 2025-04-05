t1 = float(input("Duración del primer tramo(en horas): "))
e1 = float(input("Duración de la primera escala(en horas): "))
t2 = float(input("Duración del segundo tramo(en horas): "))
e2 = float(input("Duración de la segunda escala(en horas): "))
t3 = float(input("Duración del tercer tramo(en horas): "))

total = t1 + e1
total = total + t2
total = total + e2
total = total + t3

print("Tiempo total del viaje:", total, "horas")