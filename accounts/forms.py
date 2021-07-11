from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class StaffCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','password1','password1']