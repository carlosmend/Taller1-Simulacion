import random
"""generaremos un archivo con 50000 valores pseudoaleatorios con el generador de python"""
rnP = []

for i in range(50000):
    n= random.randint(0,5000)
    rnP.append(n)

print(rnP)
numeros=open("rnP.txt","w+")
for i in rnP: 
    numeros.write(str(i))
    numeros.write(",")
numeros.close()