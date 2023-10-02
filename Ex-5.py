# Fatorial
n1 = int(input('Digite um número para calcular seu fatorial: '))

n2 = 1
while n1 > 0:
    n2 = n2 * n1
    n1 -= 1

print(f"O resultado de fatorial do numero introduzido é {n2}")


# Fatorial(2)
def factorial(n3):
    if n3 == 0:
        return 1
    else:
        return n3 * factorial(n3 - 1)


n3 = int(input('Digite um número para calcular seu fatorial: '))

print(f"O resultado de fatorial do numero introduzido é {factorial(n3)}")
