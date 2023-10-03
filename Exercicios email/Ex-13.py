# Exercicio 13 (email)
# Escreva um programa em Python que pede ao utilizador que lhe forneça
# um número e que escreve a tabuada da multiplicação para esse número.
# O seu programa deve gerar uma interacção como a seguinte:
# Escreva um numero para eu escrever a tabuada da multiplicação
# Num -> 8
# 8 x 1=8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 4 = 32
# 8 x 5 = 40
# 8 x 6 = 48
# 8 x 7 = 56
# 8 x 8 = 64
# 8 x 9 = 72
# 8 x 10 = 80
n = int(input("Digite um número: "))

for x in range(1, 11):
    print(n, "x", x, "=", n * x)
