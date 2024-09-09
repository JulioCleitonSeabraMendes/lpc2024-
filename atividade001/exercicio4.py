def le_numero():
    numero = int(input("Digite um número: "))
    lista_numeros_por_extenso = {
        0:'zero', 1:'um', 2:'dois', 3:'tres',
        4:'quatro', 5:'cinco', 6:'seis', 7:'sete',
        8:'oito', 9:'nove', 10:'dez', 11:'onze', 12:'doze',
        13:'treze', 14:'quatorze', 15:'quinze', 16:'dezesseis',
        17:'dezessete', 18:'dezoito', 19:'dezenove', 20:'vinte',
        30:'trinta', 40:'quarenta', 50:'cinquenta', 60:'sessenta',
        70:'setenta', 80:'oitenta', 90:'noventa'
        }
    if numero < 21:
        print(f'O número {numero} por extenso é {lista_numeros_por_extenso[numero]}')
    else:
        if (numero % 10) == 0:
            print(f'O número {numero} por extenso é {lista_numeros_por_extenso[numero]}')
        else:
            print(f'O número {numero} por extenso é {lista_numeros_por_extenso[((numero//10)*10)]} e {lista_numeros_por_extenso[int(str(numero)[1])]}')

le_numero()
        
