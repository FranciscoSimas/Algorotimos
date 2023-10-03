# EXERCICIO 1 (EMAIL)
# Escreva um programa em Python que pede ao utilizador que lhe forneça
# dois números (x e y) e que escreve o valor de (x + 3 * y) * (x - y).
# O seu programa deve gerar uma interação como a seguinte:
# Vou pedir-lhe dois numeros
# Escreva o primeiro numero, x = 5
# Escreva o segundo numero, y = 6
# O valor de (x + 3 * y) * (x - y) e: -23

def conta(n1, n2):
    res = (n1 + 3 * n2) * (n1 - n2)
    return res


x = float(input("Escreva o primeiro numero, x="))
y = float(input("Escreva o primeiro numero, y="))
resultado = conta(x, y)
print(f"O valor de (x + 3 * y) * (x - y) é:{resultado}")