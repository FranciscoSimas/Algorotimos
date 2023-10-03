# EXERCICIO 7 (EMAIL)
# Escreva um programa em Python que lê o número de horas, que um em-
# pregado trabalhou numa dada semana e o seu salário/hora e calcula o
# ordenado semanal tendo em conta as horas extraordinárias. O salário é
# calculado do seguinte modo: se o número de horas fôr menor que 40 então
# salário é dado pelo produto do número de horas pelo salário hora, em caso
# contrário recebe horas extraordinárias as quais são pagas a dobrar.

nome = str(input("Introduza o seu nome"))
horas = int(input(f"{nome}, introuza quantas horas trabalhou na semana"))
salario = float(input(f"{nome}, introuza o seu salário por hora"))
salario1 = 0
if horas <= 40:
    salario1 = salario * horas
elif horas > 40:
    salario_extra = (horas - 40) * (salario * 2)
    salario1 = salario_extra + (salario * 40)

print(salario1)
