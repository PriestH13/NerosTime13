from django.shortcuts import render

def dashboard(request):
    return render(request, 'base_admin/dashboard.html')
