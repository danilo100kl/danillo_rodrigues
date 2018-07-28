lista1 = input()
lista2 = input()
lista3 = ''
lista1 = lista1.split(' ')
lista1 = list(map(str, lista1))
lista2 = lista2.split(' ')
lista2 = list(map(str, lista2))
for i in lista1:
    for j in lista2:
        if(i==j):
            lista3 = lista3+str(i)+' '
print("%s\n"%lista3)
