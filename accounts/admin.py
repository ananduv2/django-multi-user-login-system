from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Staff)
admin.site.register(Courses)
admin.site.register(Batch)
admin.site.register(BatchData)
admin.site.register(Task)
admin.site.register(Student)
admin.site.register(StudentCourseData)
admin.site.register(Query)
admin.site.register(Notification)
admin.site.register(Doubt)
admin.site.register(Lead)
admin.site.register(Assignment)
admin.site.register(StudentAssignmentData)
admin.site.register(StudentProjectData)
admin.site.register(Project)
admin.site.register(CertificateTemplate)