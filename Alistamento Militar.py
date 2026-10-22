#Lê ano de nascimento de um homem e avalia a necessidade de alistamento
from datetime import date
genero = str(input('Qual é o seu gênero? \nDigite F para feminino e M para masculino: ')).upper().strip()
print('-=-' * 25)
if genero == 'F':
    print('Você não participa do alistamento obrigatório')
    print('-=-' * 25)
elif genero == 'M':
    ano = int(input('Qual o ano de nascimento? '))
    print('-=-' * 25)
    if date.today().year - ano < 18:
        print('Você tem {} anos'.format(date.today().year - ano))
        print('Você precisará se alistar em \033[1;32m{} anos\033[m \nNo ano de {}'.format(18 - (date.today().year - ano), date.today().year + (18 - (date.today().year - ano))))
    elif date.today().year - ano == 18:
        print('Você tem {} anos'.format(date.today().year - ano))
        print('\033[4;34mVocê precisa se alistar este ano!\033[m')
    elif date.today().year - ano > 18:
        print('Você tem {} anos'.format(date.today().year - ano))
        print('Você está há \033[1;31m{} anos\033[m atrasado para se alistar! \nDeveria ter se alistado em {}'.format((date.today().year - ano) - 18, ano + 18))
    print('-=-' * 25)
else:
    print('\033[1;31mOpção inválida\033[m')
    print('-=-' * 25)