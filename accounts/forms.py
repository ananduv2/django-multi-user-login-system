from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

import datetime

from django.forms import ModelForm
from .models import *

class StaffCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','password1','password1']

class AddBatchForm(ModelForm):
    class Meta:
        model = Batch
        fields ='__all__'

class TaskAllocationForm(ModelForm):
    class Meta:
        model = Task
        fields ='__all__'
        