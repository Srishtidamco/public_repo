from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import MyUser

class UserRegistraionForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'company_name','phone','password1','password2')

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    class Meta:
        model=MyUser
        fields=('email','password')
    def clean(self):
        if self.is_valid:
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid credentials")