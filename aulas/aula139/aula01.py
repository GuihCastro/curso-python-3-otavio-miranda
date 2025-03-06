"""Módulo `requests` para requisições HTTP"""

import requests # type: ignore

# url = 'https://marianalivraes.com/'
url = 'http://localhost:3000/'
response = requests.get(url)

print(response)
print(f'{response.status_code=}')
# print(response.content)
print(response.text)
