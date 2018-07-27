n = int(input())
i = 0
lista = []
while(i<n):
    lista.append(input())
    i+=1
for j in range(len(lista)-1,-1,-1):
    print(lista[j])
ultimo = len(lista)-1 
aux = lista[ultimo]
lista.insert(0,aux)
del(lista[ultimo+1])
for j in lista:
    print(j)
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
for j in lista:
    print(j)

    
    
