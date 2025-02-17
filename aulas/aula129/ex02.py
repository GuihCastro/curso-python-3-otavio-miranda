"""Data e hora atual (now), com Unix Timestamp e Timezone diferente (pytz)"""

from datetime import datetime
from pytz import timezone # type: ignore

agora = datetime.now()
agora_em_tokyo = datetime.now(timezone('Asia/Tokyo'))
print(f'{agora=}')
print(f'{agora_em_tokyo=}')
agora_formatado = agora.strftime('%d/%m/%Y %H:%M:%S')
agora_em_tokyo_formatado = agora_em_tokyo.strftime('%d/%m/%Y %H:%M:%S')
print(f'{agora_formatado=}')
dia, horas = agora_formatado.split(' ')
dia_em_tokyo, horas_em_tokyo = agora_em_tokyo_formatado.split(' ')
print(f'Agora são {horas} do dia {dia} em São Paulo/BR, e {horas_em_tokyo} do dia {dia_em_tokyo} em Tóquio/JP')
agora_em_timestamp = datetime.now().timestamp()
agora_por_timestamp = datetime.fromtimestamp(agora_em_timestamp)
agora_por_timestamp_formatado = agora_por_timestamp.strftime(
    '%d/%m/%Y %H:%M:%S')
print(f'{agora_em_timestamp=} | {agora_por_timestamp_formatado=}')
