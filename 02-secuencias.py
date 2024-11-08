import math

nombre = "\"Jorge\""

# \" comillas
# \n
# \t tabulador
# \' comillas
# print(nombre)

################################
"""
number = 2
decimal = 2.3
imaginary = 2 + 2j

print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 % 2)
print(2 ** 2)

print(round(1.7))

print(math.ceil(1.1))
print(math.pi)
"""

n1 = input("ingresa un numero: ")
n2 = input("ingresa un numero: ")

n1 = int(n1)
n2 = int(n2)

message = f"""
Resultado
SUMA {n1 + n2}
RESTA {n1 - n2}
"""



print(message)
