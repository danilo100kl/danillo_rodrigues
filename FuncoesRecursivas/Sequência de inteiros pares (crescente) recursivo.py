def soma(n,i):
  if(i+2<=n):
    print(i+2)
    soma(n,i+2)
n = int(input())
soma(n,-2)
