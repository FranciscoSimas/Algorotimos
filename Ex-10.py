# [] -> lista () -> tuplo {} -> dicionário {} -> conjunto
vendas = {}
vendas['Terceira'] = 1
vendas['Pico'] = 2
vendas['São Jorge'] = 3
# Ou vendas = {"Terceira": 1, "Pico": 2, "São Jorge": 3}

print(vendas)

ilhas = ['São Jorge', 'Faial', 'Graciosa']

for ilha in ilhas:
    vendas[ilha] = int(input(f'Vendas para {ilha}?'))

print(vendas)

for ilha in vendas:
    vendas[ilha] = vendas[ilha] * 2

print(vendas)

for k in vendas.keys():
    print(k) # Aceder ás keys

for v in vendas.values():
    print(v) # Aceder aos valores

vendas.pop("São Jorge")
print(vendas) # Retirar o valor do dicionário

vendas.popitem()
vendas.popitem()
print(vendas) # Retirar o ultimo valor do dicionário
