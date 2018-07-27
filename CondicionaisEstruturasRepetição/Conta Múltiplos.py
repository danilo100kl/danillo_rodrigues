n1 = float(input())
n2 = float(input())
i = 1
lista1 = []
lista2 = []
quant = 0
while((n1*i<50) or (n2*i<=50)):
    if(n1*i<50):
        lista1.append(n1*i)
    if(n2*i<50):
        lista2.append(n2*i)
    i+=1
for j in lista1:
    for k in lista2:
        if(j==k):
            quant+=1
print(quant)
