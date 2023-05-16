import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

def enviar(email,data_envio,hora_envio,setor,template):

    # configurações de e-mail
    de_email = 'lucas.iglesias02@gmail.com'
    de_senha = 'fzkezsexnkxhxstx'
    assunto = 'teste'
    mensagem = 'teste'
    
    
    # construir mensagem
    msg = MIMEMultipart()
    msg['From'] = de_email
    msg['To'] = email
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

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
