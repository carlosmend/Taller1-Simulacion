import numpy as np

Rn=open("Rn.txt").read()
#NumeroTxT=open("rnP.txt").read()#numeros psudoAleatorios de python
Rn=Rn.split(",")
Rn.pop()

Numero=[]
for i in Rn:
    convertirN=float(i)
    Numero.append(convertirN)
FO=[0]*10
FOA=[]
POA=[]
PEAPOA=[]


#PEA= (Ls-Li)/LSF           ls=limite superior, Li=limite inferior, LSF=limite final
PEA=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
def calcularFO():
	for i in Numero:
		if i >= 0.0 and i < 0.1:
			FO[0]+=1

		if i >= 0.1 and i < 0.2:
			FO[1]+=1

		if i >= 0.2 and i < 0.3:
			FO[2]+=1

		if i >= 0.3 and i < 0.4:
			FO[3]+=1

		if i >= 0.4 and i < 0.5:
			FO[4]+=1

		if i >= 0.5 and i < 0.6:
			FO[5]+=1

		if i >= 0.6 and i < 0.7:
			FO[6]+=1

		if i >= 0.7 and i < 0.8:
			FO[7]+=1

		if i >= 0.8 and i < 0.9:
			FO[8]+=1

		if i >= 0.9 and i <=1:
			FO[9]+=1

	calcularFOA(FO)

#Frecuencia observada acumulada ∑fi
def calcularFOA(Fo):
	foa=0
	# z=[91,102,113,110,87,95,98,104,117,83]
	
	foa=0
	for i in Fo:
		foa+=i

		FOA.append(foa)
	calcularPOA(FOA)
	

#Probabilidad observada acumulada FOA/N
def calcularPOA(foa):
	poa=0
	#z=[91,193,306,416,503,598,696,800,917,1000]
	for i in foa:
		poa=(i/foa[-1])
		POA.append(poa)
	calcularPEA_POA(PEA,POA)


def calcularPEA_POA(pea,poa):
	peapoa=0
	for i in range(len(pea)-1):
		peapoa=abs(pea[i]-poa[i])
		PEAPOA.append(peapoa)
	uniformidad()


def uniformidad():
	DMcalc=max(PEAPOA)
	print(DMcalc)
	if len(Numero)<=35:
		DMcrit=float(input(f"Por favor ingresa el DM critico para {len(Numero)} grados de libertad: "))
	else:
		DMcrit=1.36/np.sqrt(len(Numero))
	if DMcalc<=DMcrit:
		print("Si logro la prueba de uniformidad")
	else:
		print("No logro la prueba de uniformidad")

def salida():

	print("FOA: ",FOA)
	print("POA", POA)
	print("PEA", PEA)
	print("|PEA-POA|", PEAPOA)
	

calcularFO()
salida()




