"""soul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import *

urlpatterns = [
    path('', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('home/', HomeView.as_view(),name='home'),
    path('admin/', admin.site.urls),

    #common paths
    path('task/',TaskListView.as_view(),name='task'),

    #trainer
    path('trainer_dashboard/', TrainerDashboard.as_view(),name='trainer_dashboard'),
    path('trainer_registration/', TrainerRegistrationView.as_view(),name='trainer_registration'),

    #operations
    path('operations_dashboard/', OperationsDashboard.as_view(),name='operations_dashboard'),
    path('batch_register/', AllBatchView.as_view(),name='batch_register'),
    path('active_batch_register/', AllActiveBatchView.as_view(),name='active_batch_register'),
    path('batch_creation_form/', AddBatchView.as_view(),name='batch_creation_form'),
    path('batch/edit/<id>/',EditBatchView.as_view(),name='batch_edit'),
    path('batch/delete/<id>/',DeleteBatch.as_view(),name='batch_delete'),
    path('upcoming_batch_register/', AllUpcomingBatchView.as_view(),name='upcoming_batch_register'),
    path('all_trainer_list/',TrainerList.as_view(),name='all_trainer_list'),
    path('trainer_profile/<id>/',TrainerProfileView.as_view(),name='trainer_profile'),
    path('operations_registration/', OperationsRegistrationView.as_view(),name='operations_registration'),
]
