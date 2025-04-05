pelicula = float(input("Ingrese la duracion de la pelicula en minutos: "))
comerciales = float(input("Ingrese la duracion de los comerciales previos en minutos: "))
cantidad_pausas = float(input("Ingrese la cantidad de pausas comerciales: "))
duracion_pausa = float(input("Ingrese la duracion de cada pausa comercial en minutos: "))

total_comerciales = cantidad_pausas * pelicula
duracion_total = pelicula + comerciales + cantidad_pausas

print("--------calculando tus resultados------")
print("duracion de la pelicula: ", pelicula)
print("La duracion de los comerciales totales es: ", total_comerciales)
print("El tiempo total de proyeccion fue de: ", duracion_total)