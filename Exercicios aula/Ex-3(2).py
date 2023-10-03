# Calcula o salario (outros valores)
# pergunta: o nome **
#           horas **
#           preço por hora **
#           vendas **
# Seg.Social = 13%
# Horas 0 - 40  : Preço normal **
#       41 - 70 : Preço 2x **
#       71 - +  : Preço 2.5x **
# 1000  - 2%
# 2000  - 4%
# 3000  - 6%
# 4000  - 8%
# 5000<  - 10%

nome = str(input("Introduza o seu nome"))
horas = int(input(f"{nome}, introuza quantas horas trabalhou na semana"))
salario = float(input(f"{nome}, introuza o seu salário por hora"))
vendas = float(input(f"{nome}, introduza o valor de vendas"))
salario1 = 0
salario_extra1 = 0
salario_extra2 = 0
salario_vendas = 0


def calcular_salario_2(n1, n2):
    global salario1
    if n2 <= 40:
        salario1 = n1 * n2
    elif 41 <= n2 <= 70:
        salario_extra1 = (n2 - 40) * (n1 * 2)
        salario1 = (n1 * 40) + salario_extra1
    elif n2 >= 71:
        salario_extra2 = (30 * (n1 * 2)) + ((n2 - 60) * (n1 * 2.5))
        salario1 = (n1 * 40) + salario_extra2

    return salario1


calcular_salario_2(salario, horas)
print(f"Salario sem vendas = {salario1}")


def calcular_vendas_2(n1, n2):
    global salario_vendas
    if n2 <= 1000:
        vendas_extra = n2 * 0.02
        salario_vendas = n1 + vendas_extra
    elif 1000 <= n2 <= 2000:
        vendas_extra = ((n2 - 1000) * 0.04) + 1000 * 0.02
        salario_vendas = n1 + vendas_extra
    elif 2000 <= n2 <= 3000:
        vendas_extra = ((n2 - 2000) * 0.06) + 1000 * 0.04 + 1000 * 0.02
        salario_vendas = n1 + vendas_extra
    elif 3000 <= n2 <= 4000:
        vendas_extra = ((n2 - 3000) * 0.08) + 1000 * 0.06 + 1000 * 0.04 + 1000 * 0.02
        salario_vendas = n1 + vendas_extra
    elif 4000 <= n2:
        vendas_extra = ((n2 - 4000) * 0.10) + 10000 * 0.08 + 10000 * 0.06 + 10000 * 0.04 + 10000 * 0.02
        salario_vendas = n1 + vendas_extra

    return salario_vendas


calcular_vendas_2(salario1, vendas)
print(f"Salario com as vendas = {salario_vendas}")

desconto = (salario_vendas * 0.13)
print(f"Desconto para a Segurança Social = {desconto}")

liquido = salario_vendas - desconto
print(f"Total liquido = {liquido}")
