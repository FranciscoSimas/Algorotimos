# Exercicio 19 (email)
# Escreva um programa em Python que lê uma quantia em Euros e calcula
# o número de notas de 50 e, 20 e, 10 e, 5 e e moedas de 2 e, 1 e, 50
# cêntimos, 20 cêntimos, 10 cêntimos, 5 cêntimos, 2 cêntimos e 1 cêntimo,
# necessário para perfazer, essa quantia, utilizando sempre o máximo número
# de notas e moedas para cada quantia, da mais elevada, para a mais baixa.

euros = float(input("Digite a quantidade de Euros: "))
notas = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
moedas_2e = 0
moedas_1e = 0
moedas_50c = 0
moedas_20c = 0
moedas_10c = 0
moedas_5c = 0
moedas_2c = 0
moedas_1c = 0

while euros >= 50:
    euros -= 50
    notas_50 += 1
while euros >= 20:
    euros -= 20
    notas_20 += 1
while euros >= 10:
    euros -= 10
    notas_10 += 1
while euros >= 5:
    euros -= 5
    notas_5 += 1
while euros >= 2:
    euros -= 2
    moedas_2e += 1
while euros >= 1:
    euros -= 1
    moedas_1e += 1
while euros >= 0.50:
    euros -= 0.50
    moedas_50c += 1
while euros >= 0.20:
    euros -= 0.20
    moedas_20c += 1
while euros >= 0.10:
    euros -= 0.10
    moedas_10c += 1
while euros >= 0.05:
    euros -= 0.05
    moedas_5c += 1
while euros >= 0.02:
    euros -= 0.02
    moedas_2c += 1
while euros >= 0.01:
    euros -= 0.01
    moedas_1c += 1

print(f"A quantidade de notas de 50 é de {notas_50}")
print(f"A quantidade de notas de 20 é de {notas_20}")
print(f"A quantidade de notas de 10 é de {notas_10}")
print(f"A quantidade de notas de 5 é de {notas_5}")
print(f"A quantidade de moedas de 2 é de {moedas_2e}")
print(f"A quantidade de moedas de 1 é de {moedas_1e}")
print(f"A quantidade de moedas de 50c é de {moedas_50c}")
print(f"A quantidade de moedas de 20c é de {moedas_20c}")
print(f"A quantidade de moedas de 10c é de {moedas_10c}")
print(f"A quantidade de moedas de 5c é de {moedas_5c}")
print(f"A quantidade de moedas de 2c é de {moedas_2c}")
print(f"A quantidade de moedas de 1c é de {moedas_1c}")
