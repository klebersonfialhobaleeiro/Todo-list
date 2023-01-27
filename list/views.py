from datetime import datetime
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import TodoList
from django.contrib import auth
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

def home(request):
    return render(request, 'todo/home.html')

# list
@login_required(login_url='/login_and_singup')
def list(request):
    if request.method == 'GET':
        usuario = User.objects.get(id = request.user.id)
        listas = TodoList.objects.filter(dono = usuario)
        status_list = TodoList.status_choices
        
        context ={
            'listas': listas, 
            'status_list': status_list
        } 
        return render(request, 'todo/list.html', context )


def criar_item(request):
    usuariolog = User.objects.get(id = request.user.id)
    add = request.GET.get('title')

    create = TodoList.objects.create(
        title=add, 
        dono=usuariolog
    )
    nota = {
        'id': create.id ,
        'title':create.title ,
        'como':create.como ,
        'datacriacao':create.datacriacao ,
    }

    data = {'nota':nota}

    return JsonResponse(data)

@login_required(login_url='/login_and_singup')
def delete_item(request):
    todo_id  = request.GET.get('todo_id') 
    todo = TodoList.objects.get(id=todo_id)
    todo.delete()
    data = {'status':'delete'}
    return JsonResponse(data)

@login_required(login_url='/login_and_singup')
def update_item(request):  
    data_id  = request.GET.get('data_id')
    title = request.GET.get('title')

    todo = get_object_or_404(TodoList,id=data_id)
    todo.title = title
    todo.save()

    data = {'status':'update-item', 'title':title}
    return JsonResponse(data)

@login_required(login_url='/login_and_singup')
def update_status(request):  
    data_id  = request.GET.get('data_id')
    status_id = request.GET.get('status_id')
    
    todo = get_object_or_404(TodoList,id=data_id)
    todo.como = status_id
    todo.save()
    
    data = {'status':status_id}
    return JsonResponse(data)


# dashboard
def total_sum(request):
    usuario = User.objects.get(id = request.user.id)
    quantidadelist = TodoList.objects.filter(dono = usuario)
    total = len(quantidadelist)
    data = {'total': total}
    return JsonResponse(data)

def relatorio(request):
    usuario = User.objects.get(id = request.user.id)
    x = TodoList.objects.filter(dono = usuario)
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez',]
    data = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year

    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y=sum([1 for i in x if i.datacriacao.month == mes and i.datacriacao.year == ano])
        labels.append(meses [mes-1])
        data.append(y)
        cont += 1

    data_json = {'value': data[::-1], 'labels': labels[::-1]}
    return JsonResponse(data_json)

def status(request):
    usuario = User.objects.get(id = request.user.id)
    quantidadese = TodoList.objects.filter(dono = usuario , como = 'FA')
    quantidadefa = TodoList.objects.filter(dono = usuario , como = 'RE')
    quantidadefe = TodoList.objects.filter(dono = usuario , como = 'FI')

    semfazer = len(quantidadese)
    fazendo = len(quantidadefa)
    feito = len(quantidadefe)

    labels = ['a Fazer', 'Fazendo', 'Finalizado']

    data_json = {'atividade': [semfazer, fazendo, feito], 'labels':labels}
    return JsonResponse(data_json)

@login_required(login_url='/login_and_singup')
def dashboard(request):
    context = {
        'user': request.user
    }
    return render(request, 'todo/dashboard.html', context)
    

# perfil
def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    if request.method == 'POST':
        # login
        emaillog = request.POST.get('emaillog')
        passwordlog = request.POST.get('passwordlog')

        user = auth.authenticate(username=emaillog, password=passwordlog)

        if not user:
            messages.error(request, 'Usuário inválido')
            return redirect(reverse('login'))

        auth.login(request, user)
        messages.add_message(request, messages.SUCCESS, 'Usuário logado')
        return redirect(reverse('login'))
        
def register(request):
    if request.method == 'POST':      
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email)

        if user.exists():
            messages.add_message(request, messages.ERROR, 'ERRO')
            return redirect(reverse('login'))

        user = User.objects.create_user(first_name=first_name, username=email, email=email, password=password)
        messages.add_message(request, messages.SUCCESS, 'Conta criada')
        return redirect(reverse('login'))

def logout(request):
    request.session.flush()
    return redirect(reverse('login'))