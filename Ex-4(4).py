# Soluçaõ professor

def calc_seg_social(salario):
    tabela = [
        [0],
        [.11]
    ]
    descontos = 0
    for x in range(len(tabela[0])):
        if salario > tabela[0][x]:
            descontos += (salario - tabela[0][x]) * tabela[1][x]
            salario -= salario - tabela[0][x]
    return descontos


def calc_salario(horas, custo_hora):
    tabela = [
        [60, 40, 0],
        [2, 1.5, 1]
    ]

    salario = 0
    for x in range(len(tabela[0])):
        if horas > tabela[0][x]:
            salario += (horas - tabela[0][x]) * tabela[1][x] * custo_hora
            horas -= horas - tabela[0][x]
    return salario


def calc_bonus(vendas):
    comissao = [
        [40000, 30000, 20000, 10000, 0],
        [.05, .04, .03, .02, .01],
    ]

    bonus = 0
    for x in range(len(comissao[0])):
        if vendas > comissao[0][x]:
            bonus += (vendas - comissao[0][x]) * comissao[1][x]
            vendas -= vendas - comissao[0][x]
    return bonus


if __name__ == '__main__':
    # print(f'Vendas: 5000 Comissão: {calc_bonus(5000)}')
    #    print(f'Vendas: 23500 Comissão: {calc_bonus(23500)}')
    #    print(f'Vendas: 32000 Comissão: {calc_bonus(32000)}')
    #    print(f'Vendas: 50000 Comissão: {calc_bonus(50000)}')

    # print(f'horas: 20 custo: 10 salario: {calc_salario(20, 10)}')
    # print(f'horas: 40 custo: 10 salario: {calc_salario(40, 10)}')
    # print(f'horas: 50 custo: 10 salario: {calc_salario(50, 10)}')
    # print(f'horas: 60 custo: 10 salario: {calc_salario(60, 10)}')
    # print(f'horas: 80 custo: 10 salario: {calc_salario(80, 10)}')
    # print(f'horas: 100 custo: 10 salario: {calc_salario(100, 10)}')

    nome = input('Nome? ')
    horas = input('Horas? ')
    custo_hora = float(input('Custo Hora? '))
    vendas = input('Vendas? ')

    print(f'Nome: {nome}')
    print(f'Horas: {horas}')
    print(f'Vendas: {vendas}')
    o_salario = calc_salario(int(horas), custo_hora)
    print(f'Salário: {o_salario}')
    o_bonus = calc_bonus(int(vendas))
    print(f'Bónus: {o_bonus}')
    o_total = o_salario + o_bonus
    print(f'Total: {o_total}')
    o_desconto = calc_seg_social(o_total)
    print(f'Segurança Social: {o_desconto}')
    o_liquido = o_total - o_desconto
    print(f'Valor a receber: {o_liquido}')

