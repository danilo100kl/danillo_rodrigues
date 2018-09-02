import math
bin = []
def binario(n):
    global bin
    if(n>=1):
        ant = n
        n = n/2
        n = math.floor(n)
        bin.append(ant-(n*2))
        binario(n)
n = int(input())
if(n==0):
    print(0)
else:
    binario(n)
    for i in range(len(bin)-1,-1,-1):
        print(bin[i])
