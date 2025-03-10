"""Lendo arquivos com PdfReader"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger  # type: ignore

ROOT = Path(__file__).parent
PDFS_ORIGINAIS = ROOT / 'pdfs_originais'
ARQUIVOS_CRIADOS = ROOT / 'arquivos_criados'
ARQUIVOS_CRIADOS.mkdir(exist_ok=True)
IMAGENS = ARQUIVOS_CRIADOS / 'imagens'
IMAGENS.mkdir(exist_ok=True)
PDFS = ARQUIVOS_CRIADOS / 'pdfs'
PDFS.mkdir(exist_ok=True)
RELATORIO_BACEN = PDFS_ORIGINAIS / 'R20250307.pdf'

# Lendo e extraindo imagens da primeira página 
reader = PdfReader(RELATORIO_BACEN)

first_page = reader.pages[0]
first_image = first_page.images[0]
for image in first_page.images:
    with open(IMAGENS / image.name, 'wb') as img:
        img.write(image.data)
        print('Imagem salva com sucesso!')

# with open(ARQUIVOS_CRIADOS / first_image.name, 'wb') as img:
#     img.write(first_image.data)
#     print('Imagem salva com sucesso!')

# print(first_image)

# Clonando páginas e criando novos PDFs
writer = PdfWriter()
with open(PDFS / 'clone.pdf', 'wb') as file:
    for page in reader.pages:
        writer.add_page(page)
    writer.write(file)
    print('Arquivo criado com sucesso!')
    
# Desmembrando o clone
pages = []
clone = PdfReader(PDFS / 'clone.pdf')
for i, page in enumerate(clone.pages):
    writer = PdfWriter()
    pages.append(PDFS / f'page_{i+1}.pdf') # criando uma lista com os nomes dos arquivos para mergear depois
    with open(PDFS / f'page_{i+1}.pdf', 'wb') as file:
        writer.add_page(page)
        writer.write(file)
        print(f'Página {i+1} salva com sucesso!')
        
# Mergeando as páginas em um novo arquivo
pages.reverse()
merger = PdfMerger()
for page in pages:
    merger.append(page)
with open(PDFS / 'merged.pdf', 'wb') as file:
    merger.write(file)
    print('Arquivo mergeado com sucesso!')
