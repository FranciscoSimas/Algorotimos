# Exercicio 20 (email)
# Escreva um programa em Python escreve o seguinte:
# 1x8+1=9
# 12 x 8 + 2 = 98
# 123 x 8 + 3 = 987
# 1234 x 8 + 4 = 9876
# 12345 x 8 + 5 = 98765
# 123456 x 8 + 6 = 987654
# 1234567 x 8 + 7 = 9876543
# 12345678 x 8 + 8 = 98765432
# 123456789 x 8 + 9 = 987654321
# Os valores do primeiro termo da multiplicação e o resultado devem ser
# calculados pelo seu programa.
res = ""
numero = str(123456789)
for x in range(1, 10):
    res += str(x)
    print(f"{res} * 8 + {x} = {int(res) * 8 + x} ")
