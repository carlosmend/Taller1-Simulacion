import math

Numero=[]

#NumeroTxT=open("rnP.txt").read() #numeros psudoAleatorios de python
Rn=open("Rn.txt").read()
Rn=Rn.split(",")
Rn.pop()
for i in Rn:
    convertirN=float(i)
    Numero.append(convertirN)


U=0
S=0
corridas=[]
N=len(Numero)
CantCorridas=0
longitudes=[]
longitud=1
solucion=[]

corridas.append("*")
for i in range(0,len(Rn)-1):
	n1= Numero[i]
	n2= Numero[i+1]

	if n2>n1:
		corridas.append("+")

	else:
		corridas.append("-")


for i in range(0, len(corridas)-1):
	if corridas[i]==corridas[i+1]:
		longitud+=1
	elif (corridas[i] != corridas[i-1] and i+1 > len(corridas)-1) or corridas[i] != corridas[i+1]:
		CantCorridas+=1
		longitudes.append(longitud)
		longitud=1
longitudes.append(longitud)

print(longitudes)

maximo=max(longitudes)
for i in range(1,maximo+1):
	solucion.append(longitudes.count(i))
print(solucion)


U= (2*N-1)/3
S= (16*N-29)/90
Z=(CantCorridas-U)/math.sqrt(S)
#Z= (CantCorridas-U)/math.sqrt(S) 
print("")  
print("corridas: ",CantCorridas)
print("μ: ",U)
print("σ: ",S)
print("Zobs: ",Z)

if(Z<1.96 and Z>-1.96):
	print("No hay evidencia para descartar la hipotesis de independencia") 



#-----------------Mostrar comportamiento de crecimiento y decrecimiento------------------

NumColumnas=10
i=0
while True:
	print(corridas[i],end=" ") #end es para imprimir varias iteraciones en la misma fila
	i=i+1
	if i==NumColumnas or i%NumColumnas==0:
		print(" ")
	
	if i==len(Rn):
		break
#----------------------------------------------------------------------------

