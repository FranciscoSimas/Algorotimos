soma = 1
denominador = 1
print("Qual o valor de x")
x = int(input("? "))
soma += x
print("Qual o valor de n")
n = int(input("? "))

ultimoTermo = x
for pos in range(2, n + 1):
    ultimoTermo = ultimoTermo * x / pos
    soma += ultimoTermo

print("O valor da soma é ", soma)
