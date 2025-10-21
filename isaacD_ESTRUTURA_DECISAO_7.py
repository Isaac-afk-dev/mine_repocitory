#faça um programa que verifique se uma letra digitada é "f" ou "m". Conforme a letra a escrever
entrada_de_genero = float(input("Escreva genero (f)femenino, (m)masculino, (o)outros"))

if entrada_de_genero == "f":
 print(f"seu genero{entrada_de_genero} é femenino")
elif entrada_de_genero == "m":
 print(f"seu genero{entrada_de_genero} é masculino")
elif entrada_de_genero == "o":
 print(f"seu genero{entrada_de_genero} é não identificado")
else:
 print("Entrada não é válido por favor escreva (f), (m) ou (o)")