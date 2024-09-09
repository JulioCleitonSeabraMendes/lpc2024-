def le_cpf():
    cpf = input("Informe o cpf no formato xxx.xxx.xxx-xx: ")
    lista_cpf = []
    validacao_1 = False
    validacao_2 = False
    validacao_completa = False
    
    for indice in range(len(cpf)):
        if ((cpf[indice] != '.')
                and (cpf[indice] != '-')):
            lista_cpf.append(int(cpf[indice]))
        
    multiplicacao_verificacao_1 = 0
    for indice in range(10, 1, -1):
        multiplicacao_verificacao_1 += indice*lista_cpf[-(indice+1)]

    if (((multiplicacao_verificacao_1*10) % 11)
            == lista_cpf[9]):
        validacao_1 = True

    multiplicacao_verificacao_2 = 0
    for indice in range(11, 1, -1):
        a = lista_cpf[-(indice)]
        multiplicacao_verificacao_2 += indice*lista_cpf[-(indice)]

    if (((multiplicacao_verificacao_2*10) % 11)
            == lista_cpf[10]):
        validacao_2 = True
    
    if (validacao_1 and validacao_2):
        validacao_completa = True
        
    return validacao_completa

def printa_validade_cpf(validacao):
    if validacao:
        print(f'O cpf informado é válido!')
    else:
        print(f'O cpf informado é inválido!')

printa_validade_cpf(le_cpf())
