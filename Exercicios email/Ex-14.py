# Exercicio 14 (email)
# Escreva um programa que lê um inteiro e calcula a soma dos seus dígitos.

numero = input("Escreva um inteiro: ")

total = 0

for n in numero:
    total += int(n)
print("Resultado:", total)
