from DEF import ordenar

vendas = [
    # Gasolina
    [
        # OR CT OC
        [1, 2, 3, 9],  # Verão
        [4, 5, 6, 8],  # Outono
        [7, 8, 9, 700],  # Inverno
        [10, 11, 12, 6]  # Primavera
    ],
    # Gasóleo
    [
        # OR CT OC
        [13, 14, 15, 5],  # Verão
        [16, 17, 18, 4],  # Outono
        [19, 20, 21, 3],  # Inverno
        [22, 23, 24, 2]  # Primavera
    ]
]

grupos = ["Oriental", "Central", "Ocidental"]
tipos = ["Gasolina", "Gasoleo"]
estacoes = ["Verão", "Outono", "Inverno", "Primavera"]
vendasestacao = [0] * 4
casa = 0
x = y = z = 0
for y in range(len(vendas[x])):
    total2 = 0
    for x in range(len(vendas)):
        for z in range(len(vendas[x][y])):
            total2 += vendas[x][y][z]
    vendasestacao[casa] = total2
    casa += 1
    print(f"Total de vendas no(a) {estacoes[y]} = {total2}")

print(f"O maior valor de venda por estação é do valor de: [{ordenar(vendasestacao, -1)[0]}] na(s) estação(ões) :")
for x in range(len(estacoes)):
    if total2 == {ordenar(vendasestacao, -1)[0]}:
        print(x)
