# Autor: Mariana Mejía Béjar
# Calcular la distancia entre dos puntos


x1 = int(input("¿Cuál es el valor de x1: "))
y1 = int(input("¿Cuál es el valor de y1: "))
x2 = int(input("¿Cuál es el valor de x2: "))
y2 = int(input("¿Cuál es el valor de y2: "))

import math

distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)

print("La distancia es: %.3f" % distancia)