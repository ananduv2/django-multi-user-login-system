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

    def is_trainer(self):
        if self.stype == 'Trainer':
            return True
        else:
            return False

class Courses(models.Model):
    name = models.CharField(max_length=300,null=True)
    fee = models.CharField(max_length=6)

    def __str__(self):
        return self.name

class Batch(models.Model):
    mod_value= [
    ('1', 'Weekday'),
    ('2', 'Weekend')
    ]
    status_value= [
        ('Yet to start', 'Yet to start'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ]
    subject = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    trainer = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True)
    timing = models.CharField(max_length=100, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    mode = models.CharField(max_length=100,choices=mod_value,default=1)
    status = models.CharField(max_length=100,choices=status_value)

    def __str__(self):
        return "%s %s %s" %(self.trainer , self.subject , self.timing)
