from django.shortcuts import render, get_object_or_404, redirect
from .models import Diretor, Filme

def pagina_inicial(request):
    return render(request, 'index.html')

def listar_diretores(request):
    diretores = Diretor.objects.all()
    return render(request, 'diretor/listar.html', {'diretores': diretores})

def criar_diretor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        nacionalidade = request.POST['nacionalidade']
        Diretor.objects.create(nome=nome, nacionalidade=nacionalidade)
        return redirect('listar_diretores')
    return render(request, 'diretor/criar.html')

def editar_diretor(request, id):
    diretor = get_object_or_404(Diretor, id=id)
    if request.method == 'POST':
        diretor.nome = request.POST['nome']
        diretor.nacionalidade = request.POST['nacionalidade']
        diretor.save()
        return redirect('listar_diretores')
    return render(request, 'diretor/editar.html', {'diretor': diretor})

def deletar_diretor(request, id):
    diretor = get_object_or_404(Diretor, id=id)
    diretor.delete()
    return redirect('listar_diretores')

def listar_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filme/listar.html', {'filmes': filmes})

def criar_filme(request):
    diretores = Diretor.objects.all()
    if request.method == 'POST':
        titulo = request.POST['titulo']
        ano = request.POST['ano']
        diretor_id = request.POST['diretor']
        diretor = get_object_or_404(Diretor, id=diretor_id)
        Filme.objects.create(titulo=titulo, ano=ano, diretor=diretor)
        return redirect('listar_filmes')
    return render(request, 'filme/criar.html', {'diretores': diretores})

def editar_filme(request, id):
    filme = get_object_or_404(Filme, id=id)
    diretores = Diretor.objects.all()
    if request.method == 'POST':
        filme.titulo = request.POST['titulo']
        filme.ano = request.POST['ano']
        diretor_id = request.POST['diretor']
        filme.diretor = get_object_or_404(Diretor, id=diretor_id)
        filme.save()
        return redirect('listar_filmes')
    return render(request, 'filme/editar.html', {'filme': filme, 'diretores': diretores})

def deletar_filme(request, id):
    filme = get_object_or_404(Filme, id=id)
    filme.delete()
    return redirect('listar_filmes')
