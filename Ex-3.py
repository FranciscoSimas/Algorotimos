vendas = [
        # Gasolina
        [
            # OR CT OC
            [1, 2, 3],  # Verão
            [4, 5, 6],  # Outono
            [7, 8, 9],  # Inverno
            [10, 11, 12]  # Primavera
        ],
        # Gasóleo
        [
            # OR CT OC
            [13, 14, 15],  # Verão
            [16, 17, 18],  # Outono
            [19, 20, 21],  # Inverno
            [22, 23, 24]  # Primavera
        ]
]

print(f"Comprimento da lista vendas = {len(vendas)}")
print(f"Comprimento da lista vendas = {len(vendas[0])}")
print(f"Comprimento da lista vendas = {len(vendas[0][0])}")
print(f"vendas[0][0][1] = {(vendas[0][0][1])}")
print(f"vendas[1][1][1] = {(vendas[1][1][1])}")

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

print("X, Y, Z _______________________________________")

total1 = 0
for x in range(len(vendas)):
    total2 = 0
    for z in range(len(vendas[0][0])):
        total3 = 0
        for y in range(len(vendas[0])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")

print("X, Z, Y _______________________________________")

total1 = 0
for y in range(len(vendas[0])):
    total2 = 0
    for x in range(len(vendas)):
        total3 = 0
        for z in range(len(vendas[0][0])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")

print("Y, X, Z _______________________________________")

total1 = 0
for y in range(len(vendas[0])):
    total2 = 0
    for z in range(len(vendas[0][0])):
        total3 = 0
        for x in range(len(vendas)):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")

print("Y, Z, X _______________________________________")

total1 = 0
for z in range(len(vendas[0][0])):
    total2 = 0
    for x in range(len(vendas)):
        total3 = 0
        for y in range(len(vendas[0])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")

print("Z, X, Y _______________________________________")

total1 = 0
for z in range(len(vendas[0][0])):
    total2 = 0
    for y in range(len(vendas[0])):
        total3 = 0
        for x in range(len(vendas)):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")

print("Z, Y, X _______________________________________")
