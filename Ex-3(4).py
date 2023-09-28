from DEF import ordenar

vendas = [
    # Gasolina
    [
        # OR CT OC GE
        [1, 2, 3, 4],      # Verão
        [4, 5, 6, 7],      # Outono
        [7, 8, 9, 10],     # Inverno
        [10, 11, 12, 13],  # Primavera
        [2, 3, 7, 8]       # Estação Extra
    ],
    # Gasóleo
    [
        # OR CT OC   GE
        [13, 14, 15, 16],  # Verão
        [16, 17, 18, 19],  # Outono
        [19, 20, 21, 22],  # Inverno
        [22, 23, 24, 25],  # Primavera
        [9, 8, 1, 2]       # Estação Extra
    ],
    # Combustivel extra
    [
        # OR CT OC   GE
        [26, 27, 28, 29],  # Verão
        [29, 30, 31, 32],  # Outono
        [32, 33, 34, 35],  # Inverno
        [35, 36, 37, 38],  # Primavera
        [10, 9, 4, 5]      # Estação Extra
    ],
]

grupos = ["Oriental", "Central", "Ocidental", "Grupo Extra"]
tipos = ["Gasolina", "Gasoleo", "Combustivel extra"]
estacoes = ["Verão", "Outono", "Inverno", "Primavera", "Estação Extra"]
vendasestacao = [0] * len(estacoes)
vendasgrupo = [0] * len(grupos)
casa = 0
maior = 0
x = y = z = 0


# Total

total1 = 0
for x in range(len(vendas)):
    for y in range(len(vendas[x])):
        total2 = 0
        for z in range(len(vendas[x][y])):
            total1 += vendas[x][y][z]
print(f"Total de vendas = {total1}")
print()
print("_____________________________________________________")
print()

# Total por Estação

for y in range(len(vendas[x])):
    total2 = 0
    for x in range(len(vendas)):
        for z in range(len(vendas[x][y])):
            total2 += vendas[x][y][z]
    vendasestacao[casa] = total2
    casa += 1
    print(f"Total de vendas no(a) {estacoes[y]} = {total2}")

lista_ordenada_crescente, lista_original = ordenar(vendasestacao)

maior = (ordenar(vendasestacao, -1)[0][0])

print(f"O maior valor de venda por estação tem valor: {maior} na(s) estação(ões) :")

for y in range(len(lista_original)):
    if lista_original[y] == maior:
        print(estacoes[y])
print()
print("_____________________________________________________")
print()

# Total por Grupo

casa = 0
total3 = 0
menor = 0
for z in range(len(vendas[x][y])):
    total3 = 0
    for x in range(len(vendas)):
        for y in range(len(vendas[x])):
            total3 += vendas[x][y][z]
    vendasgrupo[casa] = total3
    casa += 1
    print(f"Total de vendas no grupo {grupos[z]} = {total3}")

lista_ordenada_crescente, lista_original = ordenar(vendasgrupo)

menor = (ordenar(vendasgrupo)[0][0])

print(f"O menor valor de venda por grupo tem valor: {menor} no(s) grupo(s) :")

for z in range(len(lista_original)):
    if lista_original[z] == menor:
        print(grupos[z])
