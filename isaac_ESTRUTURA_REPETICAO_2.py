#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome = print("Escreva seu nome: ")
senha = print("Escreva sua senha: ")
while nome == senha:

    print("Sua senha não  pode ser igual que o seu nome")
    print("Por favor, escreva novamente a sua senha e nome")

    nome = input("Escreva seu nome: ")
    senha = input("Escreva sua senha: ")

    print("""olá, como vai tudo?
          sua senha estará 
          em segurança conosco.""")