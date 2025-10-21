#faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo
valor_1 = float(input("escreva um número: "))
print("erro: escreva um número com valor válido")
if valor_1 > 0:
    print(f"O valor{valor_1} é positivo")
elif valor_1 < 0:
    print(f"O valor{valor_1} é negativo")
else:
    print(f"o valor é igual a 0")
