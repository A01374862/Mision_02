# Autor: Mariana Mejía Béjar, A01374862
# Calcular número total de alumnos en una clase,
# calcular el porcentaje de mujeres y hombres respectivamente

mujeres = int(input("¿Cuántas mujeres hay inscritas?: "))
hombres = int(input("¿Cuántos hombres hay inscritos?: "))

total = mujeres+hombres
porcentajeMujeres = mujeres*100/(total)
porcentajeHombres = hombres*100/(total)

print("Total de alumnos inscritos: ", total)
print("Porcentaje de mujeres: %.1f%%" % porcentajeMujeres)
print("Porcentaje de hombres: %.1f%%" % porcentajeHombres)
