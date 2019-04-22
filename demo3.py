"""
	Ejemplo de lenguaje Python
	autor:@TIMO
"""

suma = 0
multiplicacion = 0
# Pedimos que ingresen los valores
print("Ingrese el valor 1") 
valor1 = input()
print("Ingrese el valor 2") 
valor2 = input()

# Se hace la suma y la multiplicacion
suma = int(valor1) + int(valor2)
multiplicacion = int(valor1) * int(valor2)

# Imprimimos el resultado
print("la suma es: %d\tLa multiplicacion es: %d" % (suma, multiplicacion))
