from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

from .models import *
from .forms import *
# Create your views here.


class LoginView(View):
    def get(self, request):
        msg=""
        return render(request,'accounts/login.html',{'msg':msg})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            s = Staff.objects.get(user=user)
            if s.stype == "1":
                return redirect('operations_dashboard')
            elif s.stype =="2":
                return redirect('sales_dashboard')
            elif s.stype == "3":
                return redirect('trainer_dashboard')
            elif s.stype == "4":
                return render(request,'accounts/admin_dashboard.html')
        msg ="Invalid login.Check your credentials!"
        return render(request,'accounts/login.html',{'msg':msg})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class HomeView(View):
    def get(self, request):
        user = request.user
        s = Staff.objects.get(user=user)
        if s.stype == "1" :
            return redirect('operations_dashboard')
        elif s.stype == "2" :
            return redirect('sales_dashboard')
        elif s.stype == "3" :
            return redirect('trainer_dashboard')
        elif s.stype == "4" :
            return redirect('admin_dashboard')
        else:
            return redirect('logout')






# Trainer functions
class TrainerDashboard(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype =="3":
                ###Common code for trainers
                return render(request,'accounts/trainer_dashboard.html')
                ###Common code for trainers
            else:
                return redirect('home')
        else:
            return redirect('logout')


class TrainerRegistrationView(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "3":
                ###Common code for trainers
                form =StaffCreationForm()
                return render(request,'accounts/staff_registration.html',{'form':form})
                ###Common code for trainers
            else:
                return redirect('home')
        else:
            return redirect('logout')

    def post(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "3":
                ###Common code for trainers
                form =StaffCreationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    name = request.POST.get('name')
                    mobile = request.POST.get('mobile')
                    city = request.POST.get('city')
                    stype=3
                    s = Staff(user=user, name=name,mobile=mobile, city=city, stype=stype)
                    s.save()
                    return HttpResponse("Done")
                return HttpResponse("Failed")
                ###Common code for trainers
            else:
                return redirect('home')
        else:
            return redirect('logout')







# Operations Functions
class OperationsDashboard(View):
   
    def get(self, request):
        user=request.user
        s= Staff.objects.get(user=user)
        if user.is_authenticated:
            if s.stype =="1":
                ###Common code for operations
                ba=Batch.objects.filter(status=2)
                ba_count = ba.count()
                by=Batch.objects.filter(status=1)
                by_count = by.count()
                return render(request,'accounts/operations_dashboard.html',{'ba_count':ba_count,'by_count':by_count,'by':by,'ba':ba})
                ###Common code for operations
            return redirect('home')
        else:
            return redirect('logout')


class AddBatchView(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                t=Staff.objects.filter(stype="3")
                c=Courses.objects.all()
                return render(request,'accounts/batch_creation_form.html',{'t':t,'c':c})
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')

    def post(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                subject = request.POST.get('subject')
                s=Courses.objects.get(name=subject)
                trainer = request.POST.get('trainer')
                if trainer!="None":
                    t=Staff.objects.get(name=trainer)
                mod = request.POST.get('mod')
                status = request.POST.get('status')
                t=request.POST.get('timing')
                sd=request.POST.get('start_date')
                ed=request.POST.get('end_date')
                if trainer=="None":
                    b=Batch(subject=s,timing=t,start_date=sd,end_date=ed,mode=mod,status=status)
                else:
                    b=Batch(subject=s,trainer=t,timing=t,start_date=sd,end_date=ed,mode=mod,status=status)
                b.save()
                if status=="1":
                    return redirect('upcoming_batch_register')
                else:
                    return redirect('active_batch_register')
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')
                


        
class AllBatchView(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                b=Batch.objects.filter(mode="1")
                c=Batch.objects.filter(mode="2")
                return render(request,'accounts/all_batches.html',{'b':b,'c':c})
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')

class AllActiveBatchView(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                b=Batch.objects.filter(status='Ongoing',mode="1")
                c=Batch.objects.filter(status='Ongoing',mode="2")
                return render(request,'accounts/all_active_batches.html',{'b':b,'c':c})
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')


class EditBatchView(View):
    def get(self, request,id):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                b=Batch.objects.get(id=id)
                return render(request,'accounts/batch_updation_form.html',{'b':b})
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')
        



class AllUpcomingBatchView(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                b=Batch.objects.filter(status='Yet to start',mode="1")
                c=Batch.objects.filter(status='Yet to start',mode="2")
                return render(request,'accounts/all_upcoming_batches.html',{'b':b,'c':c})
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')



class OperationsRegistrationView(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                form =StaffCreationForm()
                return render(request,'accounts/staff_registration.html',{'form':form})
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')

    def post(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                form =StaffCreationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    name = request.POST.get('name')
                    mobile = request.POST.get('mobile')
                    city = request.POST.get('city')
                    stype=1
                    s = Staff(user=user, name=name,mobile=mobile, city=city, stype=stype)
                    s.save()
                    return HttpResponse("Done")
                return HttpResponse("Failed")
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')
