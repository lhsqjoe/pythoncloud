from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import SysUser


def show_login(request):
    print(SysUser.objects.all())
    return HttpResponse("Hello,world. You are at the polls index1")


def login(request):
    return render(request,'',context)

