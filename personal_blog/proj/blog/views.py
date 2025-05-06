# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Article
from .forms import ArticleForm

# Hardcoded credentials (for simplicity, use this approach only for small-scale or demo projects)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'adminpassword'

def home(request):
    articles = Article.objects.order_by('-pub_date')
    return render(request, 'home.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article.html', {'article': article})

# Admin Section (Protected) 
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Hardcoded credentials
        if username == 'admin' and password == '123':
            request.session['admin_logged_in'] = True
            return redirect('dashboard')
        else:
            return render(request, 'auth.html', {'error': 'Invalid credentials'})

    return render(request, 'auth.html')


def logout_view(request):
    request.session.flush()
    return redirect('login')

def dashboard(request):
    if not request.session.get('admin_logged_in'):
        return redirect('login')
    articles = Article.objects.all()
    return render(request, 'dashboard.html', {'articles': articles})

def add_article(request):
    if not request.session.get('admin_logged_in'):
        return redirect('login')

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm()
    
    return render(request, 'add-arti.html', {'form': form})

def edit_article(request, pk):
    if not request.session.get('admin_logged_in'):
        return redirect('login')

    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'edit-arti.html', {'form': form, 'article': article})

def delete_article(request, pk):
    if not request.session.get('admin_logged_in'):
        return redirect('login')

    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        article.delete()
        return redirect('dashboard')

    return render(request, 'del-arti.html', {'article': article})
