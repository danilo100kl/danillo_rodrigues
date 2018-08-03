entrada = int(input())
inicio = 5
contador = 0 
j=1
aux = 3
while(j*j <= entrada/2):
    if((entrada - inicio) % aux == 0):
        contador+=1
    inicio += 3
    aux += 2
    j+=1
print("%i\n"%contador)
