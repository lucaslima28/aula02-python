# print('Ola mundo')

# nota1 = float(input('Me informe sua primeira nota: '))
# nota2 = float(input('Me informe sua segunda nota: '))
# nota3 = float(input('Me informe sua terceira nota: '))

# media = (nota1 +  nota2 + nota3) / 3.0

# print('sua media foi de {}'.format(round(media,2)))

# if media == 10:
#     print('aprovado, parabens')
# elif media >= 6:
#     print('pasou raspando')
# else:
#     print('pode chorar, pegou dp')

# temparaturaC = float(input('Qual a temperatura em Celsius? '))

# temperaturaF = (temparaturaC*9/5) + 32

# print('A temperatura em fahrenheit e: {}'.format(temperaturaF))

# import math

# exponencial = math.floor(3)

# print(exponencial)

# def calcular_pagamento(qtd_horas, valor_horas):
#     horas = float(qtd_horas)
#     dinheiro = float(valor_horas)
#     if horas >= 40:
#         salario = horas * dinheiro
#     else:
#         salario = 0
#         print('voce nao recebeu nada')    
#     return salario

# salario = calcular_pagamento(40, 43.6)
# print(salario)

# detetive
# print('MEDIA MENTAL')

# perguntas = ('voce telefonou para a vitima?',
#              'voce esteve no local do crime?',
#              'voce era vizinha da vitima? ',
#              'voce tinha crush na vitima? ',
#              'Voce e o mordomo? ',
#              'voce devia dinheiros para vitima? ')

# respostas = []

# for pergunta in perguntas:
#     respostas.append(input(pergunta).upper())

# quantidade = 0
# for resposta in respostas:
#     if resposta == 'S':
#         quantidade += 1

# if quantidade < 2:
#     print('inocente')
# elif quantidade == 2:
#     print('acho q voce matou')
# elif quantidade <= 4:
#     print('voce deve ter participado do assassinato')
# else:
#         print('voce e o assassino entao voce matou')

# idade1 = float(input('Qual a sua idade mental ? '))
# idade2 = float(input('Qual a sua idade mental ? '))
# idade3 = float(input('Qual a sua idade mental ? '))
# idade4 = float(input('Qual a sua idade mental ? '))
# idade5 = float(input('Qual a sua idade mental ? '))

# media = (idade1 + idade2 + idade3 + idade4 + idade5)/5


# if media <= 25:
#     print('A sala e jovem')
# else:
#     print('A sala ta velha')



def  soma(valor1,valor2):
    return (valor1 + valor2)

valor1 = int(input('informe um valor: '))
valor2 = int(input('informe um valor: '))

print(f'A soma dos valores e {soma(valor1, valor2)}')











