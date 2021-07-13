from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Staff)
admin.site.register(Courses)
admin.site.register(Batch)
admin.site.register(Task)
admin.site.register(Student)