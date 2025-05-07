from django.shortcuts import render

def employee_list(request):
    # Esempio base; in futuro potresti passare un queryset dal DB
    return render(request, 'employees/list.html')

def employee_detail(request, employee_id):
    # Esempio con parametro; in futuro potresti usare get_object_or_404()
    return render(request, 'employees/detail.html', {'employee_id': employee_id})
