"""
Exercício - Salve sua classe em JSON
    pt.2 -> crie novamente as instâncias da classe com os dados salvos
"""

import json
from ex27_a import PATH, FamilyMember


with open(PATH, 'r', encoding='utf-8') as file:
    family = [member for member in json.load(file)]

family_members = [FamilyMember(**member) for member in family]
    
print(f'MEMBROS DA FAMÍLIA {FamilyMember.family}:')
for i, member in enumerate(family_members): print(f'\t{i} -> {vars(member)}')
    
gui = family_members[0]
print(gui.get_full_name())
