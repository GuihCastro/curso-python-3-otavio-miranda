"""Web Scraping com Python usando requests e bs4 BeautifulSoup
    * Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/

    - Web Scraping é o ato de "raspar a web" buscando informações de forma automatizada, com determinada linguagem de programação, para uso posterior;
    - O módulo requests consegue carregar dados da Internet para dentro do código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML em formato de objetos Python para facilitar a vida do desenvolvedor;

Instalação:
    - `pip install requests types-requests bs4`
"""

import re
import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

url = 'http://localhost:3000/'
response = requests.get(url)
# raw_html = response.text
bytes_html = response.content
# parsed_html = BeautifulSoup(raw_html, 'html.parser')
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{4,}', ' ', p.text))
    # print(article)
