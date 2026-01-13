import datetime


def verificar_data(dia, mes, ano, aniversario_dia, aniversario_mes):
    ano_atual = datetime.now().year
    
    # Validar ano
    if ano < ano_atual or ano > 9999:
        return "Data inválida: Ano fora do intervalo permitido."
    
    # Validar mês
    if mes < 1 or mes > 12:
        return "Data inválida: Mês fora do intervalo permitido."
    
    # Validar dia
    dias_no_mes = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Ajusta fevereiro para anos bissextos
    if mes == 2 and (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
        dias_no_mes[2] = 29
    
    if dia < 1 or dia > dias_no_mes[mes]:
        return "Data inválida: Dia fora do intervalo permitido para o mês informado."
    
    # Validar aniversário
    if dia == aniversario_dia and mes == aniversario_mes:
        return "Data válida. Essa é a data do seu aniversário!"
    else:
        return "Data válida. Essa não é a data do seu aniversário."

# Solicitar entrada do usuário
try:
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    
    # Defina aqui sua data de aniversário (dia e mês)
    aniversario_dia = 15  # Substitua pelo dia do seu aniversário
    aniversario_mes = 7   # Substitua pelo mês do seu aniversário
    
    resultado = verificar_data(dia, mes, ano, aniversario_dia, aniversario_mes)
    print(resultado)
except ValueError:
    print("Entrada inválida! Certifique-se de inserir números inteiros para dia, mês e ano.")
    
