# Autor: Mariana Mejía Béjar, A01374862
# Calcular el costo total de una comida


comida = int(input("¿Cuál es el total de su comida?: "))

propina = comida*0.13
IVA = comida*0.16
total = comida+propina+IVA


print("El costo de su comida es: $%d" % comida)
print("Propina: $%.2f" % propina)
print("IVA: $%.2f" % IVA)
print("Total a pagar: $%.2f" % total)