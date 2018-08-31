ant = 1
atual = 1
aux = 0
def fib(n,i):
    global ant, atual, aux
    if(i<n):
        aux = atual
        atual += ant
        ant = aux
        i+=1
        fib(n,i)
    else:
        print("%i mg/L"%atual)

n = int(input())
if(n == 0):
    print("O antidoto nao e necessario")
elif(n == 1 or n == 2):
    print("1 mg/L")
else:
    fib(n,2)
