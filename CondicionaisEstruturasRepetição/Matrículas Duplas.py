lista1 = []
lista2 = []
lista3 = []
n = 0
while(n<40):
    lista1.append(input())
    n+=1
n = 0
while(n<35):
    lista2.append(input())
    n+=1
for i in lista1:
    for j in lista2:
        if(i==j):
            lista3.append(i)
for j in lista3:
    print(j)
