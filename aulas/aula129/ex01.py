"""Criando datas com módulo datetime

datetime(ano, mês, dia)
datetime(ano, mês, dia, horas, minutos, segundos)
datetime.strptime('DATA', 'FORMATO')
datetime.now()
https://pt.wikipedia.org/wiki/Era_Unix
datetime.fromtimestamp(Unix Timestamp)
https://docs.python.org/3/library/datetime.html
Para timezones
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
Instalando o pytz
pip install pytz types-pytz
"""

from datetime import datetime

received_date = '10/08/1992'
date = datetime.strptime(received_date, '%d/%m/%Y')
formated_date = date.strftime('%d/%m/%Y')

print(date)
print(formated_date)
