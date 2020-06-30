from django import forms
from ApplicationUsers.models import users
class ApplicationuserForm(forms.ModelForm):
    class Meta():
        model = users
        exclude = ['first_name', 'last_name', 'status', 'email', 'password' ]