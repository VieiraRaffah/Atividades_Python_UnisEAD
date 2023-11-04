
idade_em_dias = input(f'Digite a sua idade em dias: ')

try:
    anos = int(idade_em_dias) // 365
    meses = int(idade_em_dias) // 30
    dias_restantes = (int(idade_em_dias) % 365) % 30
    idade_em_dias  = int(idade_em_dias)

    print(f"A idade é: {anos} anos, {meses} meses e {dias_restantes} dias.")   
except:
    print(f'Você não digitou um valor válido.')