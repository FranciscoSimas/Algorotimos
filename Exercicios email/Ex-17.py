# Exercicio 17 (email)
# Dado um conjunto de n inteiros representando notas de alunos, escreva
# um programa em Python para determinar quantos tiveram nota positiva.
# Modifique o seu programa de modo a também calcular qual a percentagem
# de notas positivas.
n = int(input("Digite a quantidade de notas: "))
positiva = 0
for nota in range(n):
    nota = float(input("Digite a nota: "))
    if nota >= 9.5:
        positiva += 1

percentagem = positiva / n * 100
print(f"A quantidade de notas positivas é {positiva} e a porcentagem é de {percentagem}%")
