# Autor: Mariana Mejía Béjar, A01374862
# Calcular la distancia en km que un auto recorre en 6 horas,
# calcular la distancia en km que un auto recorre en 3.5 horas,
# calcular el tiempo en horas que un auto requiere para recorrer 485 km

velocidad = int(input("Teclea la velocidad a la que viaja un auto en km/h: "))

distancia1 = velocidad*6
distancia2 = velocidad*3.5
tiempo = 485/velocidad


print("Distancia recorrida en 6 hrs: ", distancia1, "km")
print("Distancia recorrida en 3.5 hrs: ", distancia2, "km")
print("Tiempo para recorrer 485 km: %.1f" % (tiempo), "hrs.")

