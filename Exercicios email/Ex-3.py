# EXERCICIO 3.5 (EMAIL)
# Escreva um programa em Python que pede ao utilizador que lhe forneça
# um inteiro correspondente a um número de segundos e que calcula o número
# de minutos, horas e dias correspondentes a esse número de segundos. O seu programa deve permitir a interação:

segundos = float(input("Introduza um numero de segundos:"))
minutos = segundos/60
horas = minutos/60
dias = horas/24
print(f"O numero de segundos({segundos}) em minutos é: {minutos}, em horas é: {horas} e em dias é: {dias}")
