from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    phone_no = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



    
    class Meta:
        model = Account
        fields = ['username', 'email', 'phone_no', 'first_name', 'last_name', 'password1', 'password2']
