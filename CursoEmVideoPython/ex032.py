import datetime


ano = int(input('Quer ano quer analisar(YYYY)? Coloque 0 para ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Ano {ano} é BISSEXTO')
else:
    print(f'Ano {ano} não é bissexto. ')

# if ano % 400 == 0:
#     print(f'Ano {ano} é BISSEXTO')
# else:
#     if ano % 4 == 0:
#         if ano % 100 == 0:
#             print(f'Ano {ano} não é bissexto. ')
#         else:
#             print(f'Ano {ano} é BISSEXTO')
#     else:
#         print(f'Ano {ano} não é bissexto. ')
