while(1==1):
    n = int(input())
    if(n==0):
        break
    lista = input()
    listaNova = ''
    for i in range(len(lista)-1,-1,-1):
        listaNova = listaNova + lista[i]
    print(listaNova)
    
