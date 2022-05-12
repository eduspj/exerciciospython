import datetime

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento

if idade == 18:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} em {ano_atual}')
    print(f'Tem {idade} e deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} em {ano_atual}')
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será no ano de {ano_nascimento + 18}')
elif idade > 18:
    print(f'Quem nasceu em {ano_nascimento} tem {idade} em {ano_atual}')
    print(f'Você já deveria ter se alistado há {idade - 18} anos')
    print(f'Seu alistamento foi em {ano_nascimento + 18}')
