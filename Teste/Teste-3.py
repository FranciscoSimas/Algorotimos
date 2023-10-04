# EXERCICIO 3
pessoas = []
pessoa = {}
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['telefone'] = input('Telefone: ')
    pessoas.append(pessoa.copy())
    if input('Deseja inserir mais uma pessoa? ') not in ('s', 'sim'):
        break

print('--- Usando for ---')
for pessoa in pessoas:
    print(f'Nome: {pessoa["nome"]}')
    print(f'Idade: {pessoa["idade"]}')
    print(f'Telefone: {pessoa["telefone"]}')

print('--- Usando for com range ---')
for pessoa in range(len(pessoas)):
    print(f'{pessoas[pessoa]["nome"]} tem {pessoas[pessoa]["idade"]} anos e o seu telefone é {pessoas[pessoa]["telefone"]}')

print('--- Usando while ---')
x = 0
while x < len(pessoas):
    print(f'{pessoas[x]["nome"]} tem {pessoas[x]["idade"]} anos e o seu telefone é {pessoas[x]["telefone"]}')
    x += 1
