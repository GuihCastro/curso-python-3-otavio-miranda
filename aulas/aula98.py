"""
__dict__ e vars()
    -> retornam um dicionário com os atributos da instância (objeto)
"""


class Familiar:
    FAMILY = 'Henrique de Castro Livraes'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_full_name(self):
        return f'{self.name} {__class__.FAMILY}'


person_data = {'name': 'Guilherme', 'age': 32}
gui = Familiar(**person_data)
# print(gui) -> retorna metadados
print(gui.__dict__)  # retorna um dicionário com os atributos
