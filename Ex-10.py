# [] -> lista () -> tuplo {} -> dicionário {} -> conjunto
vendas = {}
vendas['Terceira'] = 1
vendas['Pico'] = 2
vendas['São Jorge'] = 3

print(vendas)

ilhas = ['São Jorge', 'Faial', 'Graciosa']

for ilha in ilhas:
    vendas[ilha] = int(input(f'Vendas para {ilha}?'))

print(vendas)

for ilha in vendas:
    vendas[ilha] = vendas[ilha] * 2

print(vendas)
