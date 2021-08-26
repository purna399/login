"""model_form_project URL Configuration

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
from .views import user_model_form ,user_form,user_html_form,get_user_list,get_single_data,update_data,delete_user,user_login,user_logout,user_send_email,verify_otp,new_password
from .views import Hello ,EmpPersonal_cls ,EmpPersonal_List ,EmpPersonal_Update ,EmpPersonal_Delete  ,EmpPersonal_Detail
urlpatterns = [
    path('model_form/',user_model_form,name='user_model_form'),
    path('form/',user_form,name='user_form'),
    path('html_form/',user_html_form,name='user_html_form'),
    path('',get_user_list,name='get_user_list'),
    path('get_single/<id>',get_single_data,name='get_single_data'),
    path('update/<id>',update_data,name='update_data'),
    path('delete/<id>',delete_user,name='delete_user'),
    path('login/',user_login,name='user_login'),
    path('logout/',user_logout,name='user_logout'),
    path('user_send_email',user_send_email,name='user_send_email'),
    path('verify_otp/',verify_otp,name='verify_otp'),
    path('new_password/<id>',new_password,name='new_password'),
    path('hello_cls',Hello.as_view(),name='hello_cls'),
    path('emp_cls_form',EmpPersonal_cls.as_view(),name='emp_cls_form'),
    path('emp_cls_list',EmpPersonal_List.as_view(),name='emp_cls_list'),
    path('emp_cls_update/<pk>',EmpPersonal_Update.as_view(),name='emp_cls_update'),
    path('emp_cls_delete/<pk>',EmpPersonal_Delete.as_view(),name='emp_cls_delete'),
    path('emp_cls_detail/<pk>',EmpPersonal_Detail.as_view(),name='emp_cls_detail')
   

    
    
    
]