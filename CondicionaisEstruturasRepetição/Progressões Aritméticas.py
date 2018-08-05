import math
quantidade = int(input())
entrada = list(map(int,input().split(' ')))
proximo=abs(entrada[0]-entrada[1])
contador=1

for i in range(quantidade-1):
    atual = abs(entrada[i]-entrada[i+1])
    if(atual!=proximo):
        contador+=1
        if(i+2!=len(entrada)):
            atual = abs(entrada[i+1]-entrada[i+2])
    proximo=atual
print(contador)
