import math

n1 = float(input('Digite um numero com casas decimais: '))
n2 = float(input('Digite para a potencia: '))
print(f'O valor "arredodando" para baixo de {n1} é {math.floor(n1)}')
print(f'O valor "arredodando" para cima de {n1} é {math.ceil(n1)}')
print(f'A raiz quadrada de {n1} é {math.sqrt(n1)}')
print(f'o numero {n1} elevado a {n2} é {math.pow(n1, n2)}')
