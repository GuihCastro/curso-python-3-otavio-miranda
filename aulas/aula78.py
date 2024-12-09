"""
Modularização
O primeiro módulo a ser executado sempre se chama `__main__`.
Podemos importar outros módulos inteiros ou partes deles para o código.
O Python conhece todo o diretório onde o __main__ está e tudo abaixo (dentro) dele.
Ele NÃO conhece os diretórios, pacotes e módulos acima do __main__.
O Python também conhece todos os pacotes e módulos presentes nos caminhos inclusos em sys.path (que podem ser alterados)
Um módulo Python é um objeto Singleton, que só é carregado uma única vez durante toda a execução do código.
Para recarregar um módulo, podemos utilizar o método `reload(<modulo>)` presente na biblioteca `importlib`.
"""

import aula78_01

print(f'Este é o módulo "{__name__}"')
print(f'E este é o módulo "{aula78_01.name}"')
print(aula78_01.somar(6, 6, 6))
