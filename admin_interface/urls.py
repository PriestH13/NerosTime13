from django.urls import path
from .views import CreateEmployeeView
from . import views

app_name = 'admin_interface'

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('create-employee/', CreateEmployeeView.as_view(), name='create_employee'),
    path('update-employee/<int:pk>/', views.UpdateEmployeeView.as_view(), name='update_employee'),
    path('delete-employee/<int:pk>/', views.DeleteEmployeeView.as_view(), name='delete_employee'),
    path('employee-list/', views.EmployeeListView.as_view(), name='employee_list'),
]
