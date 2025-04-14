from datetime import datetime

def verificar_data(dia, mes, ano, aniversario_dia, aniversario_mes):
    try:
        data = datetime(ano, mes, dia)  # Valida a data automaticamente
        msg = "Essa é a data do seu aniversário!" if (dia, mes) == (aniversario_dia, aniversario_mes) else "Essa não é a data do seu aniversário."
        return f"Data válida. {msg}"
    except ValueError:
        return "Data inválida. Verifique os valores inseridos."

# Entrada do usuário
try:
    dia, mes, ano = (int(input(f"Digite o {campo}: ")) for campo in ["dia", "mês", "ano"])
    resultado = verificar_data(dia, mes, ano, 15, 7)  # Substitua pelo seu aniversário
    print(resultado)
except ValueError:
    print("Entrada inválida! Insira números inteiros.")

