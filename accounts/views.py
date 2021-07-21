from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.db.models import Q


from .models import *
from .forms import *
from .filters import *
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
            return redirect('home')
        msg ="Invalid login.Check your credentials!"
        return render(request,'accounts/login.html',{'msg':msg})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class HomeView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            try:
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
            except:
                return redirect('student_dashboard')
        else:
            return redirect('logout')


################################################
###        Authenticated User Functions      ###
################################################
class ProfileView(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                s= Staff.objects.get(user=user)
                if s.stype =="1" or s.stype =="2" or s.stype == "3" or s.stype == "4":
                    ###Common code
                    return render(request,'accounts/profile.html',{'s':s})
                    ###Common code
                else:
                    return redirect('logout')
            except:
                return redirect('home')
        else:
            return redirect('logout')


class ProfileUpdate(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                s= Staff.objects.get(user=user)
                if s.stype =="1" or s.stype =="2" or s.stype == "3" or s.stype == "4":
                    ###Common code
                    form = ProfileUpdateForm(instance=s)
                    return render(request,'accounts/edit_profile.html',{'s':s,'form':form})
                    ###Common code
                else:
                    return redirect('logout')
            except:
                return redirect('home')
        else:
            return redirect('logout')

    def post(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                s= Staff.objects.get(user=user)
                if s.stype =="1" or s.stype =="2" or s.stype == "3" or s.stype == "4":
                    ###Common code
                    form = ProfileUpdateForm(request.POST,instance=s)
                    if form.is_valid():
                        form.save()
                        return redirect('home')
                    else:
                        return redirect('profile_update')
                    ###Common code
                else:
                    return redirect('logout')
            except:
                return redirect('home')
        else:
            return redirect('logout')



class MarkAsRead(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                ###Common code
                n= Notification.objects.filter(receiver=user)
                for i in n:
                    i.status = "Read"
                    i.save()
                return redirect('home')
                ###Common code
            except:
                return redirect('home')
        else:
            return redirect('logout')








################################################
###             Common Functions             ###
################################################
class TaskListView(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                s= Staff.objects.get(user=user)
                if s.stype =="1" or s.stype =="2" or s.stype == "3" or s.stype == "4":
                    ###Common code
                    task=Task.objects.filter(user=s).order_by('-status','created_at')
                    f=TaskFilter(self.request.GET,queryset=task)
                    task=f.qs
                    return render(request, 'accounts/task_list.html',{'task':task,'f':f})
                    ###Common code
                else:
                    return redirect('logout')
            except:
                return redirect('home')
        else:
            return redirect('logout')

class TaskView(View):
    def get(self, request,id):
        user=request.user
        if user.is_authenticated:
            try:
                s= Staff.objects.get(user=user)
                if s.stype =="1" or s.stype =="2" or s.stype == "3"  or s.stype == "4":
                    ###Common code 
                    task = Task.objects.get(id=id)
                    return render(request,'accounts/task_details.html',{'task':task})
                    ###Common code
                else:
                    return redirect('logout')
            except:
                return redirect('home')
        else:
            return redirect('logout')

class TaskUpdate(View):
    def get(self, request,id):
        user=request.user
        if user.is_authenticated:
            try:
                s= Staff.objects.get(user=user)
                if s.stype =="1" or s.stype =="2" or s.stype == "3" or s.stype == "4":
                    ###Common code 
                    task = Task.objects.get(id=id)
                    return render(request,'accounts/task_update.html',{'task':task})
                    ###Common code
                else:
                    return redirect('logout')
            except:
                return redirect('home')
        else:
            return redirect('logout')

    def post(self, request,id):
        user=request.user
        if user.is_authenticated:
            try:
                s= Staff.objects.get(user=user)
                if s.stype =="1" or s.stype =="2" or s.stype == "3" or s.stype == "4":
                    ###Common code 
                    task = Task.objects.get(id=id)
                    ns=request.POST.get('status')
                    if ns == task.status or ns =="None":
                        return redirect('task')
                    else:
                        Task.objects.filter(id=id).update(status=ns)
                        return redirect('task')
                    ###Common code
                else:
                    return redirect('logout')
            except:
                return redirect('home')
        else:
            return redirect('logout')

class StudentRegister(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                s= Staff.objects.get(user=user)
                if s.stype =="1" or s.stype =="2" or s.stype == "3" or s.stype == "4":
                    ###Common code 
                    students=Student.objects.all()
                    for i in students:
                        course_data = StudentCourseData.objects.filter(student=i)
                        i.course_enrolled=[]
                        i.now_attending=[]
                        for j in course_data:
                            i.course_enrolled.append(j.batch.subject)
                            if j.batch.status == "Ongoing":
                                i.now_attending.append(j.batch.subject)
                        i.save()
                    return render(request,'accounts/student_register.html',{'students':students})
                    ###Common code
                else:
                    return redirect('logout')
            except:
                return redirect('home')
        else:
            return redirect('logout')

                








################################################
###            Trainer Functions             ###
################################################
class TrainerDashboard(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                s= Staff.objects.get(user=user)
                if s.stype =="3":
                    ###Common code for trainers
                    return render(request,'accounts/trainer_dashboard.html')
                    ###Common code for trainers
                else:
                    return redirect('home')
            except:
                return redirect('home')
        else:
            return redirect('logout')


class TrainerRegistrationView(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                s= Staff.objects.get(user=user)
                if s.stype == "3":
                    ###Common code for trainers
                    form =StaffCreationForm()
                    return render(request,'accounts/staff_registration.html',{'form':form})
                    ###Common code for trainers
                else:
                    return redirect('home')
            except:
                return redirect('home')
        else:
            return redirect('logout')

    def post(self, request):
        user=request.user
        if user.is_authenticated:
            try:
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
                    else:
                        return HttpResponse("Failed")
                    ###Common code for trainers
                else:
                    return redirect('home')
            except:
                return redirect('home')
        else:
            return redirect('logout')






################################################
###          Operations Functions            ###
################################################
class OperationsDashboard(View):
   
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                s= Staff.objects.get(user=user)
                if s.stype =="1":
                    ###Common code for operations
                    ba=Batch.objects.filter(status="Ongoing")
                    ba_count = ba.count()
                    by=Batch.objects.filter(status="Yet to start")
                    by_count = by.count()
                    ta=Task.objects.filter(user=s).filter(~Q(status="Completed"))
                    ta_count = ta.count()
                    students=Student.objects.all()
                    note = Notification.objects.filter(receiver=user).filter(status="Not Read").order_by('-datetime')
                    no_count = note.count()
                    print(no_count)
                    for i in students:
                        course_data = StudentCourseData.objects.filter(student=i)
                        i.course_enrolled=[]
                        i.now_attending=[]
                        for j in course_data:
                            i.course_enrolled.append(j.batch.subject)
                            if j.batch.status == "Ongoing":
                                i.now_attending.append(j.batch.subject)
                        i.save()
                    return render(request,'accounts/operations_dashboard.html',{'ba_count':ba_count,'by_count':by_count,'by':by,'ba':ba,'ta':ta,'ta_count':ta_count,'students':students,'no_count':no_count,'note':note})
                    ###Common code for operations
                return redirect('home')
            except:
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
                form = AddBatchForm(instance=b)
                msg=""
                return render(request,'accounts/batch_updation_form.html',{'b':b,'form':form,'msg':msg})
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')

    def post(self, request,id):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                b=Batch.objects.get(id=id)
                form = AddBatchForm(request.POST,instance=b)
                if form.is_valid():
                    form.save()
                    s=form.cleaned_data['status']
                    if s =="Ongoing":
                        return redirect('active_batch_register')
                    else :
                        return redirect('batch_register')
                msg="Please review your edit."
                return render(request,'accounts/batch_updation_form.html',{'b':b,'form':form,'msg':msg})
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')

class DeleteBatch(View):
    def get(self, request,id):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                 b=Batch.objects.get(id=id)
                 msg="Are you sure you want to delete?"
                 return render(request,'accounts/msg.html',{'b':b,'msg':msg})
                 ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')

    def post(self, request,id):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                b=Batch.objects.get(id=id)
                b.delete()
                return redirect('operations_dashboard')
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


class TrainerList(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                t=Staff.objects.filter(stype="3")
                return render(request,'accounts/all_trainer_list.html',{'t':t})
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')

class TrainerProfileView(View):
    def get(self, request,id):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                t=Staff.objects.get(id=id)
                return render(request,'accounts/trainer_profile.html',{'t':t})
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

class QueryList(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                q=Query.objects.filter(receiver=s).filter(status="Not replied")
                return render(request,'accounts/read_queries.html',{'q':q})
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')


class ReplyQuery(View):
    def get(self, request,id):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                q=Query.objects.get(id=id)
                form = QuerySendForm(instance=q)
                return render(request,'accounts/reply_query.html',{'form':form})
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')

    def post(self, request,id):
        user=request.user
        if user.is_authenticated:
            s= Staff.objects.get(user=user)
            if s.stype == "1":
                ###Common code for operations
                q=Query.objects.get(id=id)
                q.reply=request.POST.get('reply')
                q.status="Replied"
                q.save()
                re = q.sender.user
                n = Notification(sender=user,receiver=re,content="Re : Query",subject=q.subject)
                n.save()
                return redirect('query_list')
                ###Common code for operations
            else:
                return redirect('home')
        else:
            return redirect('logout')
















################################################
###            Student Functions             ###
################################################

class StudentDashboard(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                s = Student.objects.get(user=user)
                note = Notification.objects.filter(receiver=user).filter(status="Not Read").order_by('-datetime')
                no_count = note.count()
                ###Common code for students
                scd = StudentCourseData.objects.filter(student=s)
                scd_count = scd.count()
                c = Courses.objects.all()
                q=Query.objects.filter(sender=s,status="Not replied")
                q_count = q.count()
                return render(request,'students/dashboard.html',{'s':s,'scd':scd,'scd_count':scd_count,'q_count':q_count,'no_count':no_count,'note':note})
                ###Common code for students
            except:
                return redirect('home')
        return redirect('logout')


class MyCourses(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                s = Student.objects.get(user=user)
                ###Common code for students
                scd = StudentCourseData.objects.filter(student=s).filter(batch__status="Ongoing")
                return render(request,'students/my_courses.html',{'s':s,'scd':scd})
                ###Common code for students
            except:
                return redirect('home')
        return redirect('logout')

class MyCourseList(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            try:
                s = Student.objects.get(user=user)
                ###Common code for students
                scd = StudentCourseData.objects.filter(student=s)
                scd_count = scd.count()
                c = Courses.objects.all()
                return render(request,'students/active_course_list.html',{'s':s,'scd':scd,'scd_count':scd_count})
                ###Common code for students
            except:
                return redirect('home')
        return redirect('logout')

class VideoList(View):
    def get(self, request,id): #id of batch is passed as parameter
        user=request.user
        if user.is_authenticated:
            try:
                s = Student.objects.get(user=user)
                ###Common code for students
                batch = Batch.objects.get(id=id)
                batch_data = BatchData.objects.filter(batch=batch)
                return render(request,'students/video_list.html',{'batch_data':batch_data,'batch':batch})
                ###Common code for students
            except:
                return redirect('home')
        return redirect('logout')

class PlayVideo(View):
    def get(self, request,id): 
        user=request.user
        if user.is_authenticated:
            try:
                s = Student.objects.get(user=user)
                ###Common code for students
                batch_data = BatchData.objects.get(id=id)
                scd = StudentCourseData.objects.get(student=s,batch=batch_data.batch)
                if scd.payment =="Full":
                    return render(request,'students/videoplayer.html',{'batch_data':batch_data})
                else:
                    msg="Please contact you representative!"
                    return render(request,'students/msg.html',{'msg':msg})
                ###Common code for students
            except:
                return redirect('home')
        return redirect('logout')

class SendQuery(View):
    def get(self, request): 
        user=request.user
        if user.is_authenticated:
            try:
                s = Student.objects.get(user=user)
                ###Common code for students
                form = QuerySendForm()
                st=Staff.objects.filter(stype="1")
                return render(request,'students/send_query.html',{'s':s,'form':form,'st':st})
                ###Common code for students
            except:
                return redirect('home')
        return redirect('logout')


    def post(self, request): 
        user=request.user
        if user.is_authenticated:
            try:
                s = Student.objects.get(user=user)
                ###Common code for students
                form = QuerySendForm(request.POST)
                if form.is_valid():
                    f=form.save(commit=False)
                    f.sender=s
                    f.save()
                    receiver=form.cleaned_data['receiver']
                    subject=form.cleaned_data['subject']
                    r=Staff.objects.get(name=receiver)
                    re=r.user
                    n = Notification(sender=user,receiver=re,content="Query",subject=subject)
                    n.save()
                    msg="Issue Raised"
                    return render(request,'students/msg.html',{'msg':msg})
                else:
                    msg="Failed to raise issue. Try again and mention all fields."
                    return render(request,'students/msg.html',{'msg':msg})
                ###Common code for students
            except:
                return redirect('home')
        return redirect('logout')




