"""
Closure
Funções criadas por outras funções
"""


def make_greeting(greeting):
    def greet_person(name):
        return f'{greeting}, {name}!'
    return greet_person


say_good_morning = make_greeting('Bom dia')
say_good_night = make_greeting('Boa noite')

print(say_good_morning('Guilherme'))
print(say_good_night('Mariana'))
