from django.shortcuts import render,redirect, render_to_response
from django_ajax.decorators import ajax
from Tiffin_Mgmt.models import Tiffin_Mgmt, launch_Mgmt, dinner_Mgmt

# Create your views here.
def home(request):
    print("in home")
    return render(request,'index.html')

@ajax
def add_launch(request):
    print("in add_launch")
    ldate = request.GET['ldate']
    lprice = request.GET['lprice']
    
    launch_obj = launch_Mgmt(t_date = ldate, t_price = lprice)
    launch_obj.save()
    return(1)

@ajax
def add_dinner(request):
    print("in add_dinner")
    ddate = request.GET['ddate']
    dprice = request.GET['dprice']
    
    dinner_obj = dinner_Mgmt(t_date = ddate, t_price = dprice)
    dinner_obj.save()
    return(1)