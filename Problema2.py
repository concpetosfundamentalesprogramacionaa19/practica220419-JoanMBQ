"""
	Problema 2 en python
	@autor TIMO
"""


print("Ingrese el valor de la variable X")
x = input()
print("Ingrese el valor de la variable Y")
y = input()
print("Ingrese el valor de la variable Z")
z = input()
numerador = (float(x) + float(x) / float(z))
denominador = (float(x) - float(x) / float(z))
        
m = float(numerador) / float(denominador)
        
print("el valor de m, en base a las variables:\nX=%s\n Y=%s\n  Z=%s\n da como resultado m: %.2f" % (x, y, z, m))