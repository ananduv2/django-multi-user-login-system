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

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Staff
        fields ='__all__'
        exclude = ['user','name','empid','email','sex','dob','doj','status','stype','profile_pic']

class ProfilePicChange(ModelForm):
    class Meta:
        model = Staff
        fields = ['profile_pic']
        widgets = {
            'profile_pic': forms.FileInput(),
        }

class QuerySendForm(ModelForm):
    class Meta:
        model = Query
        fields = ['sender','receiver','subject','message','reply','datetime']
        

        