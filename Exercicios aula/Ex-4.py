# Texto
# Quantas vezes aparece cada letra ?
# Apresenta do maior para o menor
# Exemplo: Escola Nova Tecnologia dos Açores
#          tem 3 vezes a letra e
#          tem 4 vezes a letra a
#          tem 5 vezes a letra o etc... etc...
# Apresenta qual letra aparece mais e menos vezes no texto

from DEF import ordenar

texto = input("Escreve um texto: ")
texto = texto.lower()
contagem = {}

for x in texto:
    if x in contagem:
        contagem[x] = contagem[x] + 1
    else:
        contagem[x] = 1

caracter = []
valores = []

for c in contagem:
    caracter = caracter + [c]
for v in contagem:
    valores = valores + [contagem[v]]

print(caracter)
print(valores)

lista_ordenada_decrescente, _ = ordenar(caracter, ordem=-1)

lista_ordenada_decrescente, _ = ordenar(valores, ordem=-1)

print(caracter)
print(valores)

for c in caracter:
    print(f"{c} aparece {contagem[c]} vezes")
