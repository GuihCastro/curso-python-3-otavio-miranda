# Constantes e boas práticas
"""
Constantes -> variáveis que não terão seu valor alterado ao longo do código
    |-> Devem ser declaradas com nome em caixa alta

Boas práticas -> devemos evitar:
    |-> Muitas condições no mesmo if
    |-> Excesso de aninhamento/complexidade
"""

# Exemplificando constantes

# Variáveis:
car_speed: float = 61.5 # velocidade de um carro
car_position: int = 99 # altura da estrada em que o carro está

# Constantes:
RADAR_SPEED: int = 60 # velocidade máxima permitida pelo radar
RADAR_POSITION: int = 100 # altura da estrada em que o radar está instalado
RADAR_RANGE: int = 1 # faixa de cobertura do radar

# Código com boas práticas
car_passed_radar = (RADAR_POSITION - RADAR_RANGE) <= car_position <= (RADAR_POSITION + RADAR_RANGE)

if car_passed_radar:
    print('O carro passou pelo radar. Checando velocidade...')
    if car_speed > RADAR_SPEED:
        print('MULTADO! Passou acima do limite.')
    else:
        print('Passou dentro do limite. Tudo certo.')
else:
    print('O carro não passou pelo radar.')
