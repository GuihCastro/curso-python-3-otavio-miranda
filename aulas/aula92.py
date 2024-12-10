"""
Salvando dados em JSON com o módulo `json`
"""

import json

person = {
    'name': 'Guilherme',
    'surname': 'Henrique de Castro',
    'addresses': [
        {'address 1': 'rua tal', 'number': 6},
        {'address 2': 'rua tal e tal', 'number': 666},
    ],
    'height': 1.69,
    'favorite_numbers': (6, 6, 6),
    'is_dev': True,
    'none': None,
}

with open('aulas\\arquivos\\aula92.json', 'w', encoding='utf-8') as file:
    json.dump(person, file, indent=2)
    
with open('aulas\\arquivos\\aula92.json', 'r', encoding='utf-8') as file:
    person_json = json.load(file)
    print(f'{person_json['name']=}')
