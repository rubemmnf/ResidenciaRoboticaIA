import calendar as c
# print(c.TextCalendar().formatmonth(2023,2))
# print(c.LocaleTextCalendar(locale='pt_BR').formatmonth(2023,2))

# print(c.weekday(2023,12,25))
# print(c.day_name[c.weekday(2035,2,29)])

mes = c.monthcalendar(2020,11)
if mes[0][c.THURSDAY]!=0:
    dia = mes[3][c.THURSDAY]
else:
    dia = mes[4][c.THURSDAY]
print(mes)
print(dia)

# def dia_thanksgiving(ano):
#     mes = c.monthcalendar(ano,11)