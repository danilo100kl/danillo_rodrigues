def romanos(vetor):
  valor = { '0':0, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000 }
  total = 0 
  ant = "0"
  aux = 0 
  for atual in vetor:
    if (atual == ant):
      aux += valor[atual]
    else:
       if (valor[atual]>valor[ant]):
          total -= aux
       else:
          total += aux
       aux = valor[atual]
       ant = atual
  total += aux
  return total
  
entrada = input()
if(romanos(entrada)%5==0):
    print("O numero e multiplo de 5!\n")
else:
    print("O resto pela divisao por 5 do numero dado e igual a %d!"%(romanos(entrada)%5))
