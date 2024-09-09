import random


def cria_lista_dados_aleatorios():
    lista_numeros_dados = []
    
    for indice in range(100):
        numero = random.randint(1,6)
        lista_numeros_dados.append(numero)
        
    return lista_numeros_dados

        
def conta_numeros_lita_dados(lista_numeros_dados):
    lista_contagem_dados = [
                    0, 0, 0,
                    0, 0, 0,
                    ]
    
    for indice in range(100):
         for numero_do_dado in range(6):
            if (lista_numeros_dados[indice]
                    == (numero_do_dado + 1)):
                lista_contagem_dados[numero_do_dado] += 1
                
    return lista_contagem_dados


def printa_frequencia_numeros(lista_contagem_dados):
    for indice in range(6):
        print(f'O {indice+1} apareceu {lista_contagem_dados[indice]} vezes!')

printa_frequencia_numeros(
    conta_numeros_lita_dados(
        cria_lista_dados_aleatorios()
        )
    )
