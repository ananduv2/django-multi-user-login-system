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

class UpdateBatchForm(ModelForm):
    class Meta:
        model = Batch
        fields =['link','status']

class TaskAllocationForm(ModelForm):
    class Meta:
        model = Task
        fields ='__all__'

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Staff
        fields ='__all__'
        exclude = ['user','name','empid','email','sex','dob','doj','status','stype','profile_pic']

class StudentProfileUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields =['dob','blood_group','mobile','house','street','street2','city','state']


class ProfilePicChange(ModelForm):
    class Meta:
        model = Staff
        fields = ['profile_pic']
        widgets = {
            'profile_pic': forms.FileInput(),
        }

class StudentProfilePicChange(ModelForm):
    class Meta:
        model = Student
        fields = ['profile_pic']
        widgets = {
            'profile_pic': forms.FileInput(),
        }

class QuerySendForm(ModelForm):
    class Meta:
        model = Query
        fields = ['sender','receiver','subject','message','reply','datetime']

class DoubtSendForm(ModelForm):
    class Meta:
        model = Doubt
        fields = '__all__'
        

class SolutionSendForm(ModelForm):
    class Meta:
        model = Doubt
        fields = ['reply']

class AddBatchData(ModelForm):
    class Meta:
        model = BatchData
        fields = ['batch','topic', 'link']

class AddStudentCourseDataForm(ModelForm):
    class Meta:
        model = StudentCourseData
        fields = ['batch','payment']
        

class LeadCreateForm(ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'

class NewStaffRegisterForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['name','empid','mobile','email','sex','doj','dob','blood_group','stype']

class AddAssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        exclude = ['link','datecreated']

        