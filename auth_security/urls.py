from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'auth_security'

urlpatterns = [
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='base_login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base_login/logout.html'), name='logout'),
    
    # Password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='base_login/password_reset.html'), name='base_login/password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='base_login/password_reset_done.html'), name='base_login/password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='base_login/password_reset_confirm.html'), name='base_login/password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='base_login/password_reset_complete.html'), name='base_login/password_reset_complete'),

    # Password change
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='base_login/password_change.html'), name='base_login/password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='base_login/password_change_done.html'), name='base_login/password_change_done'),
]