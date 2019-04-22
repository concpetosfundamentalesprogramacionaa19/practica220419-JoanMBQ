"""
	Problema 1 en python
	@autor TIMO
"""
print("Ingrese el nombre del trabajador\n") 
nombre = input()
print("Ingrese las horas Trabajadas\n")
horasTrabajadas = input()
print("Ingrese el precio por horas")
precioHoras = input()    
sueldo = float(horasTrabajadas) * float(precioHoras)
descuento = float(sueldo) * 0.10
pagar = float(sueldo) - float(descuento)

print("El valor a pagar a %s es de %.2f\n" % (nombre, pagar))