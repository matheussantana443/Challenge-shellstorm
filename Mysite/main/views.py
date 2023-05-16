from django.http import HttpResponse
from .models import Objetos, Item, Credenciais, Email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ._ataque import enviar
from django.contrib.auth.decorators import login_required
import multiprocessing

# Create your views here.
@login_required
def index(request):
    return render(request, "main/base.html", {})

# Função onde ao colocarmos o usuário admin/admin ele acessa a pagina inicial
def home(request,):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'main/base.html') 
        else:
            with open("login_invalido.txt",'a') as arquivo:
             arquivo.write(f"{username}\n")
             messages.error(request, 'Credenciais inválidas. Tente novamente.')
    return render(request, 'main/home.html')

def overview(request):
    return render(request, "main/base.html", {})

# Acesso a pagina Equipes
@login_required
def equipes(request):
    return render(request, "main/equipes.html", {})

#Teste de ataque
@login_required
def enviar_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        data_envio = request.POST.get('data_envio')
        hora_envio = request.POST.get('hora_envio')
        setor = request.POST.get('setor')
        template = request.POST.get('tipo_email')

        if template == "modelo1":
            template = "main/templates/main/teste.html"

        # criar thread para realizar o agendamento e envio do e-mail
        processo = multiprocessing.Process(target=enviar, args=(email, data_envio, hora_envio, setor, template))
        processo.start()

        return render(request, "main/ataque_sucesso.html")
    else:
        return render(request, "main/templates.html", {})

#Abrir Pagina de Conta
@login_required
def conta(request):
    return render(request, "main/conta.html", {})

#
def phishing(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        with open("captura.txt",'a') as arquivo:
            arquivo.write(f"{email}\n")

        message = 'Obrigado por se inscrever em nossa lista de e-mails!'
        return render(request, 'main/phishing.html', {'message': message})
    else:
        return render(request, 'main/phishing.html')

def sso(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        message = 'Obrigado'
        return render(request, 'main/sso.html', {'message': message})
    else:
        return render(request, 'main/sso.html')
    
#http://127.0.0.1:8000/phishing/





    
