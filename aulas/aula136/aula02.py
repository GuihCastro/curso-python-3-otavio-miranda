"""Enviando E-mails SMTP com Python"""

import os
import smtplib
from dotenv import load_dotenv  # type: ignore
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from pathlib import Path

load_dotenv()

# Caminho do arquivo HTML a ser enviado no corpo do e-mail
CAMINHO_HTML = Path(__file__).parent / 'aula02.html'

# Dados de remetente, destinatário e assunto
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente
assunto = 'teste'

# Configurações do servidor SMTP
smtp_server = os.getenv('SMTP_SERVER', '')
smtp_port = int(os.getenv('SMTP_PORT', 587))
smtp_user = remetente
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Criando a mensagem do e-mail
with open(CAMINHO_HTML, 'r', encoding='utf-8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(
        nome='Guilherme Castro', remetente='Eu mesmo')

# Transformar a mensagem em MIME
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = assunto

corpo_email = MIMEText(texto_email, 'html', 'utf-8')

mime_multipart.attach(corpo_email)

# Enviando o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    try:
        server.ehlo()
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(mime_multipart)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('E-mail não enviado...')
        print(f'Erro: {e}')
