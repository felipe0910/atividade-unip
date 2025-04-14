def avaliar_risco(idade, viajou_china, viajou_eua, lavagens_maos):
    if idade > 60:
        return "Risco alto: Paciente com mais de 60 anos"
    elif 18 <= idade <= 40 and viajou_china == "sim":
        return "Risco alto: Paciente tem entre 18 a 40 anos e já viajou para a China"
    elif idade > 40 and viajou_china == "sim":
        return "Risco médio: Paciente tem mais de 40 anos e já viajou para a China"
    elif viajou_eua == "sim" and idade < 50:
        return "Risco médio: Paciente que já viajou para os EUA e tem menos de 50 anos"
    elif idade < 25 and viajou_china == "não" and viajou_eua == "não":
        return "Risco baixo: Paciente nunca viajou para o exterior e tem menos de 25 anos"
    else:
        return "Nenhum risco identificado"

# Entrada de dados
idade = int(input("Digite a idade do paciente: "))
viajou_china = input("Já viajou para a China? (sim/não): ")
viajou_eua = input("Já viajou para os EUA? (sim/não): ")
lavagens_maos = int(input("Quantas vezes lava as mãos por dia?: "))

# Avaliação do risco
risco = avaliar_risco(idade, viajou_china, viajou_eua, lavagens_maos)
print(risco)


