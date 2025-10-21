#faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por cada aluno e apresentar:
numero_1 = float(input("Escreva número_1: "))
numero_2 = float(input("Escreva número_2: "))

if numero_1 > 7:
    print(f"Aprovado {numero_1} se a média alcançada for maior ou igual que sete")
elif numero_2 < 7: 
    print(f"reprovado {numero_2} se a média for menor que sete")
else:
    print(f"")

media = (numero_1 + numero_2) / 2
print(f"média {media}")