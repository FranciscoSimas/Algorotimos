# Calcula o salaraio
# pergunta: o nome **
#           horas **
#           preço por hora **
#           vendas **
# Seg.Social = 11%
# Horas 0 - 40  : Preço normal **
#       41 - 60 : Preço 1.5x **
#       61 - +  : Preço 2x **
# 10000  - 1%
# 20000  - 2%
# 30000  - 3%
# 40000  - 4%
# 50000<  - 5%

nome = str(input("Introduza o seu nome"))
horas = int(input(f"{nome}, introuza quantas horas trabalhou na semana"))
salario = float(input(f"{nome}, introuza o seu salário por hora"))
vendas = float(input(f"{nome}, introduza o valor de vendas"))
salario1 = 0
salario_extra1 = 0
salario_extra2 = 0
salario_vendas = 0


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


calcular_salario(salario, horas)
print(f"Salario sem vendas = {salario1}")


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


calcular_vendas(salario1, vendas)
print(f"Salario com as vendas = {salario_vendas}")

desconto = (salario_vendas * 0.11)
print(f"Desconto para a Segurança Social = {desconto}")

liquido = salario_vendas - desconto
print(f"Total liquido = {liquido}")
