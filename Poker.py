from collections import defaultdict
#Numero=open("rnP.txt").read() #numeros psudoAleatorios de python
Numero=open("Rn.txt").read() 
Numero=Numero.split(",") 
Numero.pop()
def poker_tres():
    numeros = []
    for i in Numero:
        n_temp = '{:0.3f}'.format(float(i))
        numeros.append(n_temp[2:])
    todos_diferentes = 0
    un_par = 0
    terna = 0
    for i in numeros:
        hash_map = defaultdict(lambda:0)
        for j in range(3):
            hash_map[i[j]] += 1
        tamano = len(hash_map)
        if tamano == 1:
            terna+=1
        elif tamano == 2:
            un_par+=1
        else:
            todos_diferentes += 1
    N = len(numeros)
    todos_diferentes_prob = 0.72 * N
    un_par_prob = 0.27 * N
    terna_prob = 0.01 * N
    FO = [todos_diferentes,un_par,terna]
    FE = [todos_diferentes_prob,un_par_prob,terna_prob]
    RN = []
    chi_calc = 0
    for i in range(len(FO)):
        chi_calc += ((FE[i] - FO[i]) ** 2) / FE[i]
        RN.append(chi_calc)
    chi_crit = 6.0
    if chi_calc <= chi_crit:
        print('cumple la prueba de independencia')
    else:
        print('no cumple la prueba de independencia')
    print(f'todos diferente:{todos_diferentes}\nun par:{un_par}\nterna:{terna}')
def poker_cuatro():
    numeros = []
    for i in Numero:
        n_temp = '{:0.4f}'.format(float(i))
        numeros.append(n_temp[2:])
    todos_diferentes = 0
    un_par = 0
    dos_par = 0
    terna = 0
    poker = 0
    for i in numeros:
        hash_map = defaultdict(lambda:0)
        for j in range(4):
            hash_map[i[j]] += 1
        tamano = len(hash_map)
        if tamano == 1:
            poker+=1
        elif tamano == 2:
            value = max(hash_map.values())
            if value == 3:
                terna += 1
            else:
                dos_par += 1
        elif tamano == 3:
            un_par += 1
        else:
            todos_diferentes += 1
    N = len(numeros)
    todos_diferentes_prob = 0.5040 * N
    un_par_prob = 0.4320 * N
    dos_par_pro = 0.0270 * N
    terna_prob = 0.0360 * N
    poker_pro = 0.0010 * N
    FO = [todos_diferentes,un_par,dos_par,terna,poker]
    FE = [todos_diferentes_prob,un_par_prob,dos_par_pro,terna_prob,poker_pro]
    RN = []
    chi_calc = 0
    for i in range(len(FO)):
        chi_calc += ((FE[i] - FO[i]) ** 2) / FE[i]
        RN.append(chi_calc)
    chi_crit = 9.5
    if chi_calc <= chi_crit:
        print('cumple la prueba de independencia')
    else:
        print('no cumple la prueba de independencia')

    print(f'todos diferente:{todos_diferentes}\nun par:{un_par}\ndos pares:{dos_par}\nterna:{terna}\npoker:{poker}')
def poker_cinco():
    numeros = []
    for i in Numero:
        n_temp = '{:0.5f}'.format(float(i))
        numeros.append(n_temp[2:])
    todos_diferentes = 0
    un_par = 0
    dos_par = 0
    terna = 0
    terna_par = 0
    poker = 0
    quintilla = 0
    for i in numeros:
        hash_map = defaultdict(lambda:0)
        for j in range(5):
            hash_map[i[j]] += 1
        tamano = len(hash_map)
        if tamano == 1:
            quintilla+=1
        elif tamano == 2:
            value = max(hash_map.values())
            if value == 4:
                poker += 1
            else:
                terna_par += 1
        elif tamano == 3:
            value = max(hash_map.values())
            if value == 3:
                terna += 1
            else:
                dos_par += 1
        elif tamano == 4:
            un_par += 1
        else:
            todos_diferentes += 1
    N = len(numeros)
    todos_diferentes_prob = 0.3024 * N
    un_par_prob = 0.5040 * N
    dos_par_pro = 0.1080 * N
    terna_prob = 0.0720 * N
    terna_par_pro = 0.0090 * N
    poker_pro = 0.0045 * N
    quintilla_pro = 0.0001 * N
    FO = [todos_diferentes,un_par,dos_par,terna,terna_par,poker,quintilla]
    FE = [todos_diferentes_prob,un_par_prob,dos_par_pro,terna_prob,terna_par_pro,poker_pro,quintilla_pro]
    RN = []
    chi_calc = 0
    for i in range(len(FO)):
        chi_calc += ((FE[i] - FO[i]) ** 2) / FE[i]
        RN.append(chi_calc)
    chi_crit = 12.5916
    if chi_calc <= chi_crit:
        print('cumple la prueba de independencia')
    else:
        print('no cumple la prueba de independencia')

    print(f'todos diferente:{todos_diferentes}\nun par:{un_par}\ndos pares:{dos_par}\nterna:{terna}\nterna y un par:{terna_par}\npoker:{poker}\nquintilla:{quintilla}')

def main():
    cantidad = int(input('con cuantos decimales desea realizar la prueba de poker (3-5):'))
    if cantidad == 3:
        poker_tres()
    elif cantidad == 4:
        poker_cuatro()
    elif cantidad == 5:
        poker_cinco()
    else:
        print('valor erroneo, activando auto destruccion')

if __name__ == '__main__':
    main()
