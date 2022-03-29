
Rn=[]
def Captura():
	m=int(input("Ingrese el modulo 'm' : "))  
	Xn = int(input("Introduce la semilla 'Xo: "))
	primer=Xn
	a=int(input("Introduce el multiplicador 'a': "))
	c=int(input("Introduce el incremento 'c': "))
	Validador(m,Xn,a,c)
	

#Aquí se validan las condiciones iniciales m>0, 0<=xo<m, 0<a<m, 0<=c<m
def Validador(m,Xn,a,c):
	if m<=0:
		print("Error, modulo debe ser mayor a  0, vuele a intentar")
		Captura()
	elif Xn<0 or Xn>=m:
		print("Error, Xn debe ser mayor o igual que 0 y menor que el modulo, vuelve a intentar")
		Captura()

	elif a<=0 or a>=m:
		print("Error, a debe ser mayor o que 0 y menor que el modulo, vuelve a intentar")
		Captura()

	elif c<0 or c>=m:
		print("Error, c debe ser mayor o igual que 0 y menor que el modulo, vuelve a intentar")
		Captura()
	else:
		Calculador(m,Xn,a,c)


def Calculador(m,Xn,a,c):
	primer=Xn
	count=0
	while True:
		Xn=(a*Xn+c)%m
		rn=Xn/m
		Rn.append(rn)
		print(rn)
		count+=1
		if Xn == primer:
			break


	print("El periodo es de longitud",count)
Captura()

Numero=open("Rn.txt","w+")
for i in Rn: 
    Numero.write(str(i))
    Numero.write(",")
Numero.close()



