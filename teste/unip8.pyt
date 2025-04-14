def calcular_gasto_mensal():
    # Solicita as informações do usuário
    valor_passagem = float(input("Digite o valor da passagem: "))
    passagens_por_dia = int(input("Quantas passagens você usa por dia? "))
    estudante = input("Você é estudante? (s/n): ")
    idade = int(input("Digite sua idade: "))
    
    # Aplica descontos
    if estudante == 's':
        valor_passagem *= 0.5  # Meia passagem para estudantes
    
    if idade <= 18:
        valor_passagem *= 0.1  # Apenas 10% da passagem para pessoas até 6 anos
    
    # Calcula o gasto mensal
    gasto_mensal = valor_passagem * passagens_por_dia * 30
    
    # Exibe o resultado
    print(f"Valor total gasto no mês: R$ {gasto_mensal:.2f}")

# Executa a função
calcular_gasto_mensal()











