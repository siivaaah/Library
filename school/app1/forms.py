from django import forms

from app1.models import School
from django.contrib.auth.management.commands.changepassword import UserModel
from django.forms import PasswordInput


class Schoolform(forms.ModelForm):
    location_choices=[('Ernakulam','EKM'),('Trivandrum','TVM'),('Kollam','KLM')]
    location=forms.ChoiceField(choices=location_choices,widget=forms.Select,required=True)
    class Meta:
        model=School
        fields=['name','location','principle']

class Registerform(forms.ModelForm):
    password=forms.CharField(widget=PasswordInput)
    class Meta:
        model=UserModel
        fields=['username','password','email','first_name','last_name']