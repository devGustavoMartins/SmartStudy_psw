from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(
                request, constants.ERROR, 'Senhas diferentes.'
            )
            return redirect('/usuarios/cadastro')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(
                request,
                constants.ERROR,
                'Nome de usuário indisponível.',
            )
            return redirect('/usuarios/cadastro')

        try:
            user = User.objects.create_user(
                username=username,
                password=confirmar_senha,
            )
            messages.add_message(
                request, constants.ERROR, 'Usuário cadastrado com sucesso.'
            )
            return redirect('/usuarios/logar')
        except:
            messages.add_message(
                request, constants.ERROR, 'Erro interno do sistema.'
            )
            return redirect('/usuarios/cadastro')
        
def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)
        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado com sucesso!')
            return redirect('/flashcard/novo_flashcard/')
        else:
            messages.add_message(
                request, constants.ERROR, 'Nome ou senha inválidos. '
            )
            return redirect('/usuarios/logar')
        
def logout(request):
    auth.logout(request)
    return redirect('/usuarios/logar')