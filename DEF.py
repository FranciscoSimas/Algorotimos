def ordenar(vendasestacao, ordem=1):
    # Faz uma cópia da lista original
    vendasestacao_original = vendasestacao[:]

    troquei = True
    while troquei:
        troquei = False
        x = 0
        while x < len(vendasestacao) - 1:
            if vendasestacao[x] * ordem > vendasestacao[x + 1] * ordem:
                c1 = vendasestacao[x]
                vendasestacao[x] = vendasestacao[x + 1]
                vendasestacao[x + 1] = c1
                troquei = True
            x += 1

    # Retorna a lista ordenada e a lista original
    return vendasestacao, vendasestacao_original
