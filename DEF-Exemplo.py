from DEF import ordenar

vendasestacao = [0, 2, 1, 4, 3]

# Ordena a lista de forma crescente
lista_ordenada_crescente, lista_original = ordenar(vendasestacao)
print("Lista ordenada de forma crescente:", lista_ordenada_crescente)

# Retorna à ordem original
print("Lista original:", lista_original)

# Ordena a lista de forma decrescente
lista_ordenada_decrescente, _ = ordenar(vendasestacao, ordem=-1)
print("Lista ordenada de forma decrescente:", lista_ordenada_decrescente)

# Retorna à ordem original
print("Lista original:", lista_original)
