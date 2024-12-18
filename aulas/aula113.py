"""
Polimorfismo em Python Orientado a Objetos

Polimorfismo é o princípio que permite que classes deridavas de uma mesma superclasse tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes.
    -> Assinatura do método = Mesmo nome e quantidade de parâmetros

SO|->L<-|ID
Princípio da substituição de Liskov
    -> Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação.
    
    * Sobrecarga de métodos (overload)  🐍 = ❌
    * Sobreposição de métodos (override) 🐍 = ✅
"""

from abc import ABC, abstractmethod


class Notificacao:
    def __init__(self, mensagem):
        self._mensagem = mensagem
        
    @property
    def mensagem(self):
        return self._mensagem
    
    @abstractmethod
    def enviar(self) -> bool: ...
    
    
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        try: 
            print(f'E-MAIL -> Notificação: {self.mensagem}')
            return True
        except Exception as error:
            print(f'ERRO -> {error.__class__.__name__}: {error}')
            return False
        
        
class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        try:
            print(f'SMS -> Notificação: {self.mensagem}')
            return True
        except Exception as error:
            print(f'ERRO -> {error.__class__.__name__}: {error}')
            return False
        
        
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    print('Notificação enviada com sucesso!' if notificacao_enviada else 'Notificação NÃO enviada!')
    
    
notificar(NotificacaoEmail('Testando E-MAIL...'))
notificar(NotificacaoSMS('Testando SMS...'))
