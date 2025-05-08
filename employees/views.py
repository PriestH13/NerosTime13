from django.shortcuts import render

def employee_list(request):
    return render(request, 'base_employees/list.html')

def employee_detail(request, employee_id):
    return render(request, 'base_employees/detail.html', {'employee_id': employee_id})

def employee_dashboard(request):
    return render(request, 'base_employees/dashboard.html')
