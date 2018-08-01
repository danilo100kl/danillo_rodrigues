quant = int(input())
lista = input()
lista = lista.split(' ')
lista = list(map(float, lista))
lista.sort()
total = 1
listaNova = []
if(quant <= 2):
    print(total)
else:
    valor = lista[1] - lista[0]
    for i in range(quant-1):
        if(valor != (lista[i+1] - lista[i])):


____________________________________________________________
            if(i == quant-1):
                valor = lista[i+1] - lista[i]
                listaNova.append(valor)
            elif():
____________________________________________________________


    listaNova.sort()
    for i in range(len(listaNova)-1):
        if(listaNova[i] != listaNova[i+1]):
            total += 1
    print(total)

