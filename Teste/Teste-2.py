# EXERCICIO 2
ilhas = [0] * 5
distancias = [0] * 5
max = 0
min = 0
x = 0
for i in range(5):
    ilha = input("Introduza o nome da ilha do grupo central")
    distancia = int(input(f"Introduza a distância da ilha do grupo central em relação a São Miguel"))
    ilhas[i] = ilha
    distancias[i] = distancia
for ilha in ilhas:
    if x == 0:
        min = distancias[x]
        max = distancias[x]
    else:
        if distancias[x] < min:
            min = distancias[x]
        if distancias[x] > max:
            max = distancias[x]
    x += 1

for x in range(len(distancias)):
    if distancias[x] == max:
        ilhas_max = ilhas[x]
for x in range(len(distancias)):
    if distancias[x] == min:
        ilhas_min = ilhas[x]

print(f"A ilha que fica mais perto de São Miguel é {ilhas_min} e fica a {min} de distância")
print(f"A ilha que fica mais mais longe de São Miguel é {ilhas_max} e fica a {max} de distância")
