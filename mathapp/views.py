from django.shortcuts import render

# Create your views here.

def addnumber(request):
    context = {}
    return render(request,'mathapp/addnumber.html',context)

def volumecylinder(request):
    context = {}
    return render(request,'mathapp/volumecylinder.html',context) 