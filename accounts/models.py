from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Staff(models.Model):
    value= (
    ('1', 'Operations'),
    ('2', 'Sales'),
    ('3', 'Trainer'),
    ('4', 'Admin'),
    )
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
    groups = (
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        )

    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    empid = models.CharField(max_length=100,null=True, blank=True)
    mobile = models.CharField(max_length=10,null=True, blank=True)
    email = models.EmailField(max_length=200,null=True, blank=True)
    sex = models.CharField(max_length=10,null=True,choices=(('Male','Male'),('Female','Female')), blank=True)
    dob = models.DateField(null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=100,null=True, blank=True,choices=groups)
    house = models.CharField(max_length=100,null=True, blank=True)
    street =models.CharField(max_length=100,null=True, blank=True)
    street2 =models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True,choices=state, blank=True)
    stype = models.CharField(max_length=100,null=True,choices=value, blank=True)
    status = models.CharField(max_length=20,choices=(('Active','Active'),('Inactive','Inactive')),default='Active')
    profile_pic = models.ImageField(null=True, blank=True,default="student.jpg")

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
    link = models.CharField(max_length=1000,null=True, blank=True)
    pic = models.ImageField(null=True, blank=True)

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
    link = models.CharField(max_length=1000,null=True,blank=True)
    passcode = models.CharField(max_length=100,null=True,blank=True,default="N/A")
    mode = models.CharField(max_length=100,choices=mod_value,default=1)
    status = models.CharField(max_length=100,choices=status_value)

    def __str__(self):
        return "%s %s %s %s" %(self.trainer , self.subject , self.start_date , self.timing)


class BatchData(models.Model):
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True)
    topic = models.CharField(max_length=100,null=True)
    link = models.CharField(max_length=1000,null=True, blank=True)
    datecreated = models.DateField(null=True,blank=True,auto_now_add=True)

    def __str__(self):
        return "%s %s" %(self.batch , self.topic)

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
    user= models.OneToOneField(User,on_delete=models.CASCADE,null=True)
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
    status = models.CharField(max_length=20,choices=(('Active','Active'),('Inactive','Inactive')),default='Active')
    profile_pic = models.ImageField(null=True,blank=True,default="")

    def __str__(self):
        return self.name


class StudentCourseData(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='student',null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE,related_name='batch')
    payment = models.CharField(max_length=10,choices=(('Full','Full'),('Half','Half'),('Not Paid','Not Paid')),default='Not Paid')
    
    def __str__(self):
        s=" 's "
        return "%s %s %s" % (self.student,s, self.batch)


class Query(models.Model):
    sender = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='sender',null=True,blank=True)
    receiver = models.ForeignKey(Staff,on_delete=models.CASCADE,related_name='receiver',null=True,limit_choices_to={'stype':"1"})
    subject = models.CharField(max_length=400,null=True)
    message = models.TextField(max_length=1500,null=True)
    reply = models.TextField(max_length=1500, null=True, blank=True)
    datetime = models.DateField(default=datetime.datetime.now(),null=True, blank=True)
    status = models.CharField(max_length=100,choices=(('Not replied','Not replied'),('Replied','Replied')),default='Not replied',blank=True)

    def __str__(self):
        return "%s %s" % (self.sender,self.subject)