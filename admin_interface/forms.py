from django import forms
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password
    
    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user