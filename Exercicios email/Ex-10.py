# Exercicio 10 (email)
# Escreva um programa em Python que lê um número inteiro positivo e
# calcula o número obtido do número lido que apenas contém os seus dígitos
# impares. Por exemplo,
# Escreva um inteiro
# ? 785554
# Resultado: 7555

numero = input("Escreva um inteiro: ")

n_pares = ""
n_impares = ""

for n in numero:
    if int(n) % 2 != 0:
        n_impares += n

print("Resultado:", n_impares)


# 1 3 7 8* 10 13 14 17 19 20