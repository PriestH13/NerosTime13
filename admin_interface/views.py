from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import EmployeeForm

class AdminOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        # Solo superuser o staff abilitato
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("Non hai i permessi per accedere a questa pagina.")

class CreateEmployeeView(LoginRequiredMixin, AdminOnlyMixin, CreateView):
    model = User
    form_class = EmployeeForm
    template_name = 'base_admin/create_employee.html'

    success_url = reverse_lazy('admin_interface:create_employee')

    def form_valid(self, form):
        return super().form_valid(form)


def dashboard(request):
    return render(request, 'base_admin/dashboard.html')

class UpdateEmployeeView(LoginRequiredMixin, AdminOnlyMixin, UpdateView):
    model = User
    form_class = EmployeeForm
    template_name = 'base_admin/update_employee.html'
    success_url = reverse_lazy('admin_interface:update_employee')

    def get_object(self, queryset=None):
        user = super().get_object(queryset)
        return user 

    def form_valid(self, form):
        return super().form_valid(form)
    
class DeleteEmployeeView(LoginRequiredMixin, AdminOnlyMixin, DeleteView):
    model = User
    template_name = 'base_admin/delete_employee.html'
    success_url = reverse_lazy('admin_interface:admin_dashboard')

    def get_object(self, queryset=None):
        user = super().get_object(queryset)
        return user
    
class EmployeeListView(LoginRequiredMixin, AdminOnlyMixin, ListView):
    model = User
    template_name = 'base_admin/list_employees.html'
    context_object_name = 'employees'