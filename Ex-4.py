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

if horas <= 40:
    salario1 = salario * horas
elif 41 <= horas <= 60:
    salario_extra1 = (horas - 40) * (salario * 1.5)
    salario1 = (salario * 40) + salario_extra1
elif horas >= 61:
    salario_extra2 = (20 * (salario * 1.5)) + ((horas - 60) * (salario * 2))
    salario1 = (salario * 40) + salario_extra2

print(f"Salario sem vendas = {salario1}")

if vendas <= 10000:
    vendas_extra = vendas * 0.01
    salario_vendas = salario1 + vendas_extra
elif 10000 <= vendas <= 20000:
    vendas_extra = ((vendas - 10000) * 0.02) + 10000 * 0.01
    salario_vendas = salario1 + vendas_extra
elif 20000 <= vendas <= 30000:
    vendas_extra = ((vendas - 20000) * 0.03) + 10000 * 0.02 + 10000 * 0.01
    salario_vendas = salario1 + vendas_extra
elif 30000 <= vendas <= 40000:
    vendas_extra = ((vendas - 30000) * 0.04) + 10000 * 0.03 + 10000 * 0.02 + 10000 * 0.01
    salario_vendas = salario1 + vendas_extra
elif 40000 <= vendas:
    vendas_extra = ((vendas - 40000) * 0.05) + 10000 * 0.04 + 10000 * 0.03 + 10000 * 0.02 + 10000 * 0.01
    salario_vendas = salario1 + vendas_extra

print(f"Salario com as vendas = {salario_vendas}")

desconto =(salario_vendas * 0.11)
print(f"Desconto para a Segurança Social = {desconto}")

liquido = salario_vendas - desconto
print(f"Total = {liquido}")
