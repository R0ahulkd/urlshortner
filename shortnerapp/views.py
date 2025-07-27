from django.shortcuts import render, redirect
from .forms import RegisterForm, URLForm
from django.contrib.auth import authenticate, login, logout
from .models import URL
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = URLForm()
    urls = URL.objects.filter(user=request.user)
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.user = request.user
            url.save()
    return render(request, 'home.html', {'form': form, 'urls': urls})

def redirect_view(request, code):
    try:
        url = URL.objects.get(short_code=code)
        url.clicks += 1
        url.last_accessed = timezone.now()
        url.save()
        return HttpResponseRedirect(url.original_url)
    except URL.DoesNotExist:
        raise Http404("Invalid Short URL")

from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    urls = URL.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'urls': urls})

from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

@login_required
def delete_url_view(request, pk):
    url = get_object_or_404(URL, pk=pk)
    if url.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this URL.")
    url.delete()
    return redirect('dashboard')

from django.shortcuts import render

def about_view(request):
    return render(request, 'about.html')
