def identificar_bandeira(numero_cartao):
    numero = str(numero_cartao)
    if numero.startswith('8'):
        return 'Voyager'
    elif numero.startswith('6062'):
        return 'Hypercard'
    elif numero.startswith('4'):
        return 'Visa'
    elif numero.startswith('50'):
        return 'Aura'
    elif numero.startswith('21'):
        return 'EnRout'
    elif numero.startswith(('51', '52', '53', '54', '55')):
        return 'MasterCard'
    elif numero.startswith(('34', '37')):
        return 'American Express'
    elif numero.startswith('6011') or numero.startswith('65'):
        return 'Discover'
    elif numero.startswith('35'):
        return 'JCB'
    elif numero.startswith('36') or numero.startswith('38'):
        return 'Diners Club'
    else:
        return 'Bandeira desconhecida'

# Exemplo de uso
numero = input("Digite o número do cartão: ")
print(identificar_bandeira(numero))