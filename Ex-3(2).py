vendas = [
    # Gasolina
    [
        # V  O  I  P
        [1, 4, 7, 10],  # Oriental
        [2, 5, 8, 11],  # Central
        [3, 6, 9, 12],  # Ocidental
    ],
    # Gasóleo
    [
        # V   O   I    P
        [13, 16, 19, 22],  # Oriental
        [14, 17, 20, 23],  # Central
        [15, 18, 21, 24],  # Ocidental
    ]
]

grupos = ["Oriental", "Central", "Ocidental"]
tipos = ["Gasolina", "Gasoleo"]


x = y = z = 0
total1 = 0
for x in range(len(vendas)):
    total2 = 0
    for y in range(len(vendas[0])):
        total3 = 0
        for z in range(len(vendas[0][0])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")
print()
print(f"Comprimento da lista vendas = {len(vendas)}")
print(f"Comprimento da lista vendas = {len(vendas[0])}")
print(f"Comprimento da lista vendas = {len(vendas[0][0])}")


