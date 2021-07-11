from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from .models import *
from .forms import *
# Create your views here.
class TrainerCheck(UserPassesTestMixin, View):

    def test_func(self):
        user=request.user
        s= Staff.objects.get(user=user)
        if s.stype !=3:
            return redirect('login')
        pass

    


class LoginView(View):
    def get(self, request):
        return render(request,'accounts/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            s = Staff.objects.get(user=user)
            if s.stype == "1":
                return render(request,'accounts/operations_dashboard.html')
            elif s.stype =="2":
                return render(request,'accounts/sales_dashboard.html')
            elif s.stype == "3":
                return render(request,'accounts/trainer_dashboard.html')
            elif s.stype == "4":
                return render(request,'accounts/admin_dashboard.html')
            else:
                return redirect('/')
            return redirect('/')
        return HttpResponse("Failed")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class HomeView(View):
    def get(self, request):
        user = request.user
        s = Staff.objects.get(user=user)
        if s.stype == "1":
            return render(request,'accounts/operations_dashboard.html')
        elif s.stype =="2":
            return render(request,'accounts/sales_dashboard.html')
        elif s.stype == "3":
            return render(request,'accounts/trainer_dashboard.html')
        elif s.stype == "4":
            return render(request,'accounts/admin_dashboard.html')
        else:
            return redirect('/')
        return redirect('/')



class TrainerRegistrationView(LoginRequiredMixin,View):


    def get(self, request):
        form =StaffCreationForm()
        return render(request,'accounts/staff_registration.html',{'form':form})

    def post(self, request):
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


class OperationsRegistrationView(View):

    def get(self, request):
        form =StaffCreationForm()
        return render(request,'accounts/staff_registration.html',{'form':form})

    def post(self, request):
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
