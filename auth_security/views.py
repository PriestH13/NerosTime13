from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('core_home')
        else:
            return render(request, 'base_login/login.html', {
                'error': 'Credenziali non valide'
            })
    return render(request, 'base_login/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
