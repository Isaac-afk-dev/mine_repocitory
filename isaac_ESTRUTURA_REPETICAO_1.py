#faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue até o usuario mostrar um valor válido.
while True:
    valor = int(input("Digite uma nota entre 0 e 10: "))
    if valor >= 0 and valor <=10:
        break