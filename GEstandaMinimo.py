import numpy as np

x=int (input("Por favor ingresa la semilla: "))
print("")

a=int (input("Por favor ingresa el multiplicador: "))
print("")

m=int (input("Por favor ingresa el modulo: "))
print("")

decision= input("Desea ingresar el r y q")
if decision == "si":
    q=int (input("Por favor ingresa q: "))
    r=int (input("Por favor ingresa r: "))
else:
    q=np.floor(m/a)
    q=int(q)

    r=m%a

Rn=[]
Almacen=[x]
while True: 
    Xn1= a*(x%q)-r* np.floor(x/q)
    if len(Almacen)==50000:
        break
   
    if Xn1 < 0:
        Xn1+=m

    if Xn1 in Almacen:
        break
    else: 
        Almacen.append(Xn1)
        x=Xn1
        rn=x/m
        Rn.append(rn)

print(Almacen)
input()
print(Rn)

Numero=open("Rn.txt","w+")
for i in Rn: 
    Numero.write(str(i))
    Numero.write(",")
Numero.close()