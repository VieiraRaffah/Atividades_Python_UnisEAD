def frase_inverter(frase):
    palavras = frase.split()
    invertida = ' '.join([palavra[::-1] for palavra in palavras])
    return invertida

frase_usuario = input(f'Digite a Frase que deseja inverter: ')
frase_final = frase_inverter(frase_usuario)

print(f'Essa é a Frase que você digitou: {frase_usuario}')
print(f'Essa é a a sua Frase invertida: {frase_final}')
