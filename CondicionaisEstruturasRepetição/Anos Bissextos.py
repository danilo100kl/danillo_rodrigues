anoI = int(input())
anoF = int(input())
bissexto = False
while(anoI<=anoF):
    if(anoI%4==0):
        print(anoI,"\n")
        anoI+=4
        bissexto = True
    else:
        anoI+=1
if(bissexto==False):
    print("-1\n")
