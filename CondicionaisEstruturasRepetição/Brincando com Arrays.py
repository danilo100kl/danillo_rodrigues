n = int(input())
novaLista = []
lista = (input())
lista = lista.split(' ')
lista = list(map(int, lista))
for j in range(len(lista)-1,-1,-1):
    novaLista.append(lista[j])
novaLista = str(novaLista).strip('[]').replace(',', '')
print(novaLista)
ultimo = len(lista) 
lista.insert(ultimo,lista[0])
del(lista[0])
novaLista = str(lista).strip('[]').replace(',', '')
print(novaLista)
for j in range (len(lista)-1):
    aux1 = False
    for k in range (len(lista)-1):
        if(lista[k] < lista[k+1]):
            aux2 = lista[k]
            lista[k] = lista[k+1]
            lista[k+1] = aux2
            aux1 = True
    if(aux1 == False):
        break
novaLista = str(lista).strip('[]').replace(',', '')
print(novaLista)
