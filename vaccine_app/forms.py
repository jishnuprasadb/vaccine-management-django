from django import forms
from django.contrib.auth.forms import UserCreationForm

from vaccine_app.models import Login, User, Vaccine, Nurse, Hospital


class LoginRegister(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

class UserRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=('name','email','phone_number','age','address')

class Vaccine_Add(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ('name','description')

class NurseRegistration(forms.ModelForm):
    class Meta:
        model=Nurse
        fields=('name','email','age','phone_number','address')

class HospitalRegistration(forms.ModelForm):
    class Meta:
        model=Hospital
        fields=('name','place','contact','email')


