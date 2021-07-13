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
    trainer = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True,limit_choices_to={'stype':"3"})
    timing = models.CharField(max_length=100, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    mode = models.CharField(max_length=100,choices=mod_value,default=1)
    status = models.CharField(max_length=100,choices=status_value)

    def __str__(self):
        return "%s %s %s" %(self.trainer , self.subject , self.timing)

class Task(models.Model):
    status_value= [
        ('Yet to start', 'Yet to start'),
        ('In progress', 'In progress'),
        ('Completed', 'Completed'),
    ]
    user = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=500,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    assigned_by = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True,related_name='sender')
    status = models.CharField(max_length=100,choices=status_value,default='Yet to start')

    def __str__(self):
        return "%s %s" %(self.user , self.title)
    
    class Meta:
        ordering=['created_at','-status']



class Student(models.Model):
    state = (
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal')
)
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    sex = models.CharField(max_length=10,null=True,choices=(('Male','Male'),('Female','Female')))
    house = models.CharField(max_length=100,null=True)
    street =models.CharField(max_length=100,null=True)
    street2 =models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True,choices=state)
    course_enrolled = models.CharField(max_length=100,null=True)
    now_attending = models.CharField(max_length=100,null=True)
    start_date = models.DateField(null=True)
    shared = models.BooleanField(default=False,choices=((True, 'Yes'), (False, 'No')))
    payment = models.CharField(max_length=10,choices=(('Full','Full'),('Half','Half')),default='Half')

    def __str__(self):
        return self.name