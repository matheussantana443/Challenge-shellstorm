import smtplib
import datetime
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string


def abrir_arquivo(arquivo) -> str:
    try:
        with open(arquivo,"r") as doc:
            envio = doc.read()
            return envio
    except:
        print("arquivo com problemas confira o codigo e o path")

def enviar(email, data_envio, hora_envio, setor, template):
    # configurações de e-mail
    de_email = 'lucas.iglesias02@gmail.com'
    de_senha = 'fzkezsexnkxhxstx'
    assunto = 'teste'
    #mensagem = 'teste'
    mensagem = abrir_arquivo(template)
    # construir mensagem
    msg = MIMEMultipart()
    msg['From'] = de_email
    msg['To'] = email
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'html'))

    # converter data_envio e hora_envio para um objeto datetime
    data_hora_envio = datetime.datetime.strptime(data_envio + " " + hora_envio + ":00", '%Y-%m-%d %H:%M:%S')

    # verificar se a hora de envio já passou
    agora = datetime.datetime.now()
    if data_hora_envio < agora:
        print('Erro: a data e hora de envio devem ser no futuro')
        return

    # esperar até o horário programado
    while True:
        agora = datetime.datetime.now()
        if agora >= data_hora_envio:
            break
        time.sleep(60) # esperar 1 minuto antes de verificar novamente

    # conectar ao servidor SMTP do Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(de_email, de_senha)

    try:
        # enviar mensagem
        smtp.sendmail(de_email, email, msg.as_string())
    except Exception as e:
        print('Erro ao enviar e-mail: ' + str(e))
    finally:
        smtp.quit()
