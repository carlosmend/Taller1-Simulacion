import numpy as np
#NumeroTxT=open("rnP.txt").read() #numeros psudoAleatorios de python
NumeroTxT=open("Rn.txt").read()
NumeroTxT=NumeroTxT.split(",")
NumeroTxT.pop()

Numero=[]
for i in NumeroTxT:
    convertirN=float(i)
    Numero.append(convertirN)

print("PRUEBA DE SERIE")
Nparejas= len(Numero)//2
Nclases=10
FE=Nparejas/(Nclases**2)
FO=np.zeros((Nclases,Nclases)) #matriz que se inicializa en 0

Lparejas=[]
for i in range(0,Nparejas,2):#toma desde el inicio y luego va de dos en dos
    Lparejas.append((Numero[i],Numero[i+1]))

IntervaloS=1/10
IntervaloI=0
Fila=0

while IntervaloS <=1:

    Columna=0
    ColumnaI=0
    ColumnaS=1/10
    NTemporal=[]

    for i in range(len(Lparejas)):
        if Lparejas [i][0] >= IntervaloI and Lparejas [i][0] < IntervaloS:
            NTemporal.append(Lparejas[i])
#Se busco en todas las parejas, las que cumplen con el x en el intervalo.

    while ColumnaS <=1:
        for i in range(len(NTemporal)):
            if NTemporal [i][1] >= ColumnaI and NTemporal [i][1] < ColumnaS:
                FO[Fila,Columna]+=1
#Contamos las frecuencias obtenidas

        ColumnaI = ColumnaS
        ColumnaS+=1/10
        Columna+=1
    Fila+=1
    IntervaloI = IntervaloS
    IntervaloS+=1/10

TablaChi=((FE-FO)**2)/FE
Xcal=np.sum(TablaChi)
Xcrit= 124.3421

if Xcal <= Xcrit:
    print("Paso la prueba")
else:
    print("No paso la prueba")

print(FE)
input()
print(FO)
input()
print(TablaChi) 