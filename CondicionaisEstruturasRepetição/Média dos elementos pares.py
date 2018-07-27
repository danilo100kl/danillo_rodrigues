media = 0
quant = 0
vetor = (input())
vetor = vetor.split(' ')
vetor = list(map(int, vetor))
for i in vetor:
    if(i>0 and i%2==0):
        media = media + i
        quant+=1
if(media==0):
    print("-1\n")
else:
    media=media/quant
    print("%.2f\n"%media)
