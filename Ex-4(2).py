salarios = [11, 25, 5, 6, 10]
empregados = ["Francisco", "João", "Leandro", "Rafel", "Gonçalo"]

nome = str(input("Introduza o seu nome"))
for empregado in range(len(empregados)):
    if nome == empregados[empregado]:
        horas = int(input(f"{empregados[empregado]}, introuza quantas horas trabalhou na semana"))
        vendas = float(input(f"{empregados[empregado]}, introduza o valor de vendas"))
else:
    print(f"O nome {nome} não foi encontrado na empresa")


salario1 = 0
salario_extra1 = 0
salario_extra2 = 0
salario_vendas = 0

for empregado in range(len(empregados)):
    if nome == empregados[empregado]:
        if horas <= 40:
            salario1 = horas * salarios[empregado]
        elif 41 <= horas <= 60:
            salario_extra1 = (horas - 40) * salarios[empregado]
            salario1 = (salarios[empregado] * 40) + salario_extra1
        elif horas >= 61:
            salario_extra2 = (20 * (salarios[empregado] * 1.5)) + ((horas - 60) * (salarios[empregado] * 2))
            salario1 = (salarios[empregado] * 40) + salario_extra2

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
