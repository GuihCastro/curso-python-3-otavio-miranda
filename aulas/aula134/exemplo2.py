"""Módulo secrets"""
# O módulo secrets é capaz de fazer tudo o que o módulo random faz, porém de forma mais segura.

import secrets
import string

# cria um "random seguro", baseado no sistema operacional
random = secrets.SystemRandom()
chave_segura = ''.join(random.choices(
    string.ascii_letters + string.digits + string.punctuation,
    k=16
))

print(chave_segura)
