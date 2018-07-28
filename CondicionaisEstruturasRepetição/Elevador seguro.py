quant = 0
peso = 0
novoPeso = 1
while((quant < 7) and (peso < 560) and (novoPeso != 0)):
    novoPeso = float(input())
    quant+=1
    peso = peso + novoPeso
if(peso>560):
    peso = peso - novoPeso
    quant-=1
elif(novoPeso==0):
    quant-=1
print("%i\n%.1f"%(quant,peso))
