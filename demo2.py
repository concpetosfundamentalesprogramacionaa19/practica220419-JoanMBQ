"""
	Ejemplo de lenguaje Python
	autor:@TIMO
"""

import sys

nombre_archivo = sys.argv[0]
valor1 = sys.argv[1]
valor2 = sys.argv[2]

suma = int(valor1) + int(valor2)
multiplicacion = int(valor1) * int(valor2)

print("la suma es: %s" % suma) 
print("La multiplicacion es: %s"  % multiplicacion)
