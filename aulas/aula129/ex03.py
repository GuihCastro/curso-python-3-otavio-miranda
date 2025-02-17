"""Timedelta (calculos com datas)

datetime.timedelta e dateutil.relativetimedelta (calculando datas)
Docs:
https://dateutil.readthedocs.io/en/stable/relativedelta.html
https://docs.python.org/3/library/datetime.html#timedelta-objects
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta # type: ignore

fmt = '%d/%m/%Y %H:%M:%S'
meu_nascimento = datetime.strptime('10/08/1992 16:31:00', fmt)
nascimento_mari = datetime.strptime('20/03/1992 03:15:00', fmt)
diferenca = relativedelta(meu_nascimento, nascimento_mari)
print(diferenca)
