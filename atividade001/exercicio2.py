def le_caracteres():
    caracteres = input("Digite a sequência de caracteres a serem analisados: ")
    caracteres_sem_espaco = []
    
    for indice in range(len(caracteres)):
        if (caracteres[indice]
                != ' '):
            caracteres_sem_espaco.append(caracteres[indice])
            
    return caracteres_sem_espaco, caracteres

def analise_se_eh_palindromo(caracteres_sem_espaco):
    tamanho_caracteres = len(caracteres_sem_espaco)
    palindromo = False
    
    if ((tamanho_caracteres % 2)
            == 0):
        tamanho_caracteres_por_2 =  int(tamanho_caracteres / 2)
        contador = 0
        
        for indice in range(tamanho_caracteres_por_2):
            if (caracteres_sem_espaco[indice]
                    == caracteres_sem_espaco[-1 - (indice)]):
                contador += 1
                
        if (contador == tamanho_caracteres_por_2):
            palindromo = True

    else:
        tamanho_caracteres_por_2 =  int((tamanho_caracteres / 2) -1)
        contador = 0
        
        for indice in range(tamanho_caracteres_por_2):
            if (caracteres_sem_espaco[indice]
                    == caracteres_sem_espaco[-1 - (indice)]):
                contador += 1
                
        if (contador == tamanho_caracteres_por_2):
            palindromo = True


    return palindromo

def printa_se_eh_polindromo(palindromo, caracteres):
    if palindromo:
        print(f'O conjundo de caracteres "{caracteres}" é políndromo')
    else:
        print(f'O conjundo de caracteres "{caracteres}" não é políndromo')

caracteres_sem_espaco, caracteres = le_caracteres()

printa_se_eh_polindromo(
    analise_se_eh_palindromo(caracteres_sem_espaco),
    caracteres)
                
            
        
