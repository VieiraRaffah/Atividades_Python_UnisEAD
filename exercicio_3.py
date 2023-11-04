try:
    num_1 = int(input(f'Digite um número inteiro: '))
    num_2 = int(input(f'Digite outro número inteiro: '))
    num_3 = int(input(f'Digite outro número inteiro: '))
    
    menor_numero = min(num_1,num_2,num_3)

    print(f'O menor número entre, {num_1}, {num_2} e {num_3}, é {menor_numero}.')
except:
    print(f'Os valores digitados não são válidos.')