# Autor: Mariana Mejía Béjar
# Calcular cuántos ingredientes se 
# requieren para hacer galletas

galletas = int(input("Teclee el número de galletas que desee hacer: "))

azúcar = galletas*1.5/48
mantequilla = galletas*1/48
harina = galletas*2.75/48

print("El número de tazas de azúcar requerido es: ", azúcar)
print("El número de tazas de mantequilla requerido es: ", mantequilla)
print("El número de tazas de harina requerido es: ", harina)