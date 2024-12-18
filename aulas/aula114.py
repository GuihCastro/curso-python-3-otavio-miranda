"""
Criando Exceptions em Python Orientado a Objetos

Para criar uma Exception em Python, só precisamos herdar de alguma exceção da linguagem.
A recomendação da doc é herdar de Exception.
https://docs.python.org/3/library/exceptions.html

    -> Criando exceções (comum colocar Error ao final)
    -> Levantando (raise)
    -> Lançando (throw)
    -> Relançando exceções
    -> Adicionando notas em exceções (3.11.0)
"""


class MyError(Exception): ...
    
    
class AnoterError(Exception): ...


def raise_error():
    exception_ = MyError('Minha mensagem de erro...')
    exception_.add_note('Nota do meu erro...')
    raise exception_


try:
    raise_error()
except (MyError, ZeroDivisionError) as error:
    print(f'{error.__class__.__name__}: {error.args}\n')
    exception_ = AnoterError('Relançado meu erro...')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Outra nota do meu outro erro...')
    raise exception_ from error
