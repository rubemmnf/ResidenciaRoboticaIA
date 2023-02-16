# from datetime import datetime
# hoje = datetime.now()
# print(hoje)

from datetime import date
hoje = date.today()
# print(hoje)
ano = 1985
mes = 3
dia = 28
data_nascimento = date(ano, mes, dia)
# print(data_nascimento)
dias = hoje - data_nascimento
print(type(dias.days))

teste = False
print(type(teste))
if isinstance(teste, bool):
    print('tem um booleano')