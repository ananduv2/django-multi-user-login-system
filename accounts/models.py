from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Staff(models.Model):
    value= [
    ('1', 'Operations'),
    ('2', 'Sales'),
    ('3', 'Trainer'),
    ('4', 'Admin'),
]
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=10,null=True)
    city = models.CharField(max_length=100,null=True)
    stype = models.CharField(max_length=100,null=True,choices=value)


    def __str__(self):
        return self.name