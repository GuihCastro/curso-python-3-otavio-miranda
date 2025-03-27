"""Redimensionando imagens com o Pillow"""
# Essa biblioteca é o "Photoshop do Python"

from pathlib import Path
from PIL import Image  # type: ignore

ROOT = Path(__file__).parent
ORIGINAL = ROOT / 'original.jpg'
NEW = ROOT / 'new.jpg'

img = Image.open(ORIGINAL)
width, height = img.size
exif = img.info['exif']

print(f'Imagem original: {width}x{height}')
new_width = int(input('Escolha um novo valor para a largura da imagem: '))
new_height = round(new_width * height / width)
new_size = (new_width, new_height)

new_img = img.resize(new_size)
new_img.save(
    NEW,
    optimize=True,
    quality=70,
    exif=exif
)

print(
    f'Imagem redimensionada com sucesso para o tamanho: {new_width}x{new_height} !')
