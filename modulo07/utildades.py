'''
Potenciaçao

Divisao

Multiplicaçao

Soma

Subtraçao
'''


def soma(a,b):

    return a + b

def potenciaçao(a,b):
    return a + b

def divisao(a,b):
    return a / b 

def multiplicaçao(a,b):
    return a * b 

def subtraçao(a,b):
    return a - b

def calcular_media(lista_numeros):

    if not lista_numeros:
        return 0 
    return sum(lista_numeros) / len(lista_numeros)


def e_par(numero):
    return numero % 2 == 0 

def divisao_inteira(a,b):
    if b == 0:
        return "Erro divisao por zero nao e permitida."
    return a // b 

def resto_divisao(a, b):
    if b == 0:
        return "Erro Divisao por zero nao e permitida."
    return a % b 

def potencia(base , expoente):
    return base ** expoente 


import utildades
import datetime
from faker import Faker


fake = Faker('pt_BR') 


print('***Dados Criados - Prova de Matematica')
print(f'Nome De Mentira: {fake.name()}')
print(f'Email De Mentira: {fake.email()}')
print(f'Telefone De Mentira: {fake.fone()}')


print(f'Dados Da Prova De Mentira ***')
agora = datetime.datetime.now()
print(f'Data e Hora Da Prova: {agora.strftime("%d/%m/%Y %H:%M:%S")}')