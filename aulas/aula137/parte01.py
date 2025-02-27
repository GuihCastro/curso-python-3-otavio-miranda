"""ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile"""
# Criando caminhos e arquivos

from pathlib import Path

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_PACOTE = CAMINHO_RAIZ / 'pacote'
CAMINHO_ZIP = CAMINHO_RAIZ / 'pacote.zip'

# Criando o pacote que será compactado
CAMINHO_PACOTE.mkdir(exist_ok=True)


# Função para popular o pacote
def popular_pacote(qtd: int, dir: Path):
    for i in range(qtd):
        texto = f'Teste {i+1}'
        caminho = dir / f'arquivo_{i+1}.txt'
        with caminho.open('w', encoding='utf-8') as arquivo:
            arquivo.write(texto)
