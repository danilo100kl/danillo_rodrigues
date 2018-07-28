anos = (input())
anos = anos.split(' ')
anos = list(map(int, anos))
anoI = anos[0]
anoF = anos[1]
bissexto = False
while(anoI<=anoF):
    if(anoI%400==0):
        print("%i"%anoI)
        anoI+=4
        bissexto = True
    elif(anoI%4==0 and anoI%100!=0):
        print("%i"%anoI)
        anoI+=4
        bissexto = True
    else:
        anoI+=1
if(bissexto==False):
    print("-1")
print("\n")
