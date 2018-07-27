n = int(input())
i = 0
v = []
nova = []
while(n!=0):
    v = input()
    for j in range((len(v)-1),-1,-1):
        nova.append(v[j])
    print(nova)
    nova.clear()
    n = int(input())

