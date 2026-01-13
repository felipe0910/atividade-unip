soma_idades = 0
idade_usuario = int(input("Digite sua idade: "))

while True:
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    curso = input("Curso do aluno: ")
    
    if idade >= idade_usuario:
        soma_idades += idade
    
    continuar = input("Deseja parar? (S para sim, qualquer outra tecla para continuar): ")
    if continuar == "S":
        break

print(f"A soma das idades dos alunos com idade maior ou igual a {idade_usuario} é: {soma_idades}")
