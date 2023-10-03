def calcular_salario(n1, n2):
    global salario1
    if n2 <= 40:
        salario1 = n1 * n2
    elif 41 <= n2 <= 60:
        salario_extra1 = (n2 - 40) * (n1 * 1.5)
        salario1 = (n1 * 40) + salario_extra1
    elif n2 >= 61:
        salario_extra2 = (20 * (n1 * 1.5)) + ((n2 - 60) * (n1 * 2))
        salario1 = (n1 * 40) + salario_extra2

    return salario1


def calcular_vendas(n1, n2):
    global salario_vendas
    if n2 <= 10000:
        vendas_extra = n2 * 0.01
        salario_vendas = n1 + vendas_extra
    elif 10000 <= n2 <= 20000:
        vendas_extra = ((n2 - 10000) * 0.02) + 10000 * 0.01
        salario_vendas = n1 + vendas_extra
    elif 20000 <= n2 <= 30000:
        vendas_extra = ((n2 - 20000) * 0.03) + 10000 * 0.02 + 10000 * 0.01
        salario_vendas = n1 + vendas_extra
    elif 30000 <= n2 <= 40000:
        vendas_extra = ((n2 - 30000) * 0.04) + 10000 * 0.03 + 10000 * 0.02 + 10000 * 0.01
        salario_vendas = n1 + vendas_extra
    elif 40000 <= n2:
        vendas_extra = ((n2 - 40000) * 0.05) + 10000 * 0.04 + 10000 * 0.03 + 10000 * 0.02 + 10000 * 0.01
        salario_vendas = n1 + vendas_extra

    return salario_vendas
