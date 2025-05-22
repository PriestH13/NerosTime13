from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    template_name = 'base_login/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core_home')  # Cambia con la tua url di home dopo login
        else:
            context = {'error': 'Credenziali non valide'}
            return render(request, self.template_name, context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
