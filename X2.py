#NumeroTxT=open("rnP.txt").read() #numeros psudoAleatorios de python
NumeroTxT=open("Rn.txt").read() 
NumeroTxT=NumeroTxT.split(",")
NumeroTxT.pop()

Numero=[]
for i in NumeroTxT:
    convertirN=float(i)
    Numero.append(convertirN)

print("PRUEBA X2")
Xcrit=16.92
FE=len(Numero)/10.0
FO=[0]*10
for i in Numero:
    if i >= 0.0 and i < 0.1:
        FO[0]+=1
    elif i >= 0.1 and i < 0.2:
        FO[1]+=1
    elif i >= 0.2 and i < 0.3:
        FO[2]+=1
    elif i >= 0.3 and i < 0.4:
        FO[3]+=1
    elif i >= 0.4 and i < 0.5:
        FO[4]+=1
    elif i >= 0.5 and i < 0.6:
        FO[5]+=1
    elif i >= 0.6 and i < 0.7:
        FO[6]+=1
    elif i >= 0.7 and i < 0.8:
        FO[7]+=1
    elif i >=0.8 and i < 0.9:
        FO[8]+=1
    elif i >=0.9 and i <= 1:
        FO[9]+=1

FEFO=[]

def fefo(FE,FO):
    return ((FE-FO)**2)/FE

for i in FO:
    FEFO.append(fefo(FE,i))

Xcal=sum(FEFO)
if Xcal <= Xcrit:
    print ("Cumple la prueba de uniformidad")
else: print ("No cumple la prueba de uniformidad")

print("FE", FE)
input()
print("FO",FO)
input()
print("FEFO", FEFO)   
input() 
print("Xcal" , Xcal)
