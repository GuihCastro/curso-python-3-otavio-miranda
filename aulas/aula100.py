"""
`method` vs. `@classmethod` vs. `@staticmethod`
    -> `method` -> usa `self` e tem acesso ao escopo da instância;
    -> `@classmethod` -> usa `cls` e tem acesso ao escopo da classe;
    -> `@staticmethod` -> não usa nada e não tem acesso a nada.
"""


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # method -> tem acesso ao `self` / instância
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod  # -> tem acesso à `cls` / classe
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod  # -> não tem acesso a nada
    def log(msg, name):
        print(f'LOG: {msg}\nUSER: {name}')


c1 = Connection()
c1.set_user('Guilherme')
c1.set_password('666')

c2 = Connection.create_with_auth('Mariana', '123456')

c1.log('Mensagem foda', c1.user)
c2.log('Outra mensagem foda', c2.user)
