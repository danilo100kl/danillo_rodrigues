ant = 1
atual = 1
i = 2
n = int(input())
if(n == 0):
    print("O antidoto nao e necessario")
elif(n == 1):
    print("1 mg/L")
else:
    while(i<n):
        aux = atual
        atual += ant
        ant = aux
        i+=1
    print("%i mg/L"%atual)
