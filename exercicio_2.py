try:
    valor_a = float(input(f'Digite um valor: '))
    valor_b = float(input(f'Digite outro valor: '))
    valor_c = float(input(f'Digite outro valor: '))
    nao_tringulo = valor_a > (valor_b + valor_c)

    if not nao_tringulo:    
        calc = (valor_a + valor_b + valor_c) /2
        area = (calc * (calc * valor_a) * (calc - valor_b) * (calc - valor_c))
        print(f'A área do triângulo é: {area:.2f}')
    else:
        print(f'Os valores {valor_a}, {valor_b}, {valor_c} não formam um triângulo.')
except:
    print(f'Os valores digitados não são válidos.')    