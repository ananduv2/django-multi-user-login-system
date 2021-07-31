import django_filters
from django_filters import CharFilter

from .models import *


class TaskFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title',lookup_expr='icontains')
    class Meta:
        model = Task
        fields = '__all__'
        exclude =['created_at']

class StudentFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains')
    now_attending = CharFilter(field_name='now_attending',lookup_expr='icontains')
    class Meta:
        model = Student
        fields = ['name','email','course_enrolled','now_attending','status']

class LeadFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains')
    mobile = CharFilter(field_name='mobile',lookup_expr='icontains')
    email = CharFilter(field_name='email',lookup_expr='icontains')
    class Meta:
        model = Lead
        fields = '__all__'
        exclude =['created_on']

class StaffFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains')
    mobile = CharFilter(field_name='mobile',lookup_expr='icontains')
    email = CharFilter(field_name='email',lookup_expr='icontains')
    class Meta:
        model = Staff
        fields = ['name','email','mobile']
        
    

