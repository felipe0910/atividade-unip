def calcular_total_fraldas(idade_meses):
    total_fraldas = 0
    
    if idade_meses <= 2:
        total_fraldas = idade_meses * 220
    elif 3 <= idade_meses <= 8:
        total_fraldas = (2 * 220) + ((idade_meses - 2) * 180)
    elif 9 <= idade_meses <= 24:
        total_fraldas = (2 * 220) + (6 * 180) + ((idade_meses - 8) * 150)
    else:
        total_fraldas = (2 * 220) + (6 * 180) + (16 * 150)
    
    return total_fraldas

# Entrada do usuário
idade_meses = int(input("Digite a idade do seu filho em meses: "))

# Cálculo e exibição do resultado
total_fraldas = calcular_total_fraldas(idade_meses)
print(f"Total de fraldas usadas até o momento: {total_fraldas}")

