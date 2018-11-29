from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from .models import SysUser


def show_login(request):
    # print(SysUser.objects.all())
    # return HttpResponse("Hello,world. You are at the polls index1")
    return render_to_response("login.html")


# 用户登录
# def login(request,username, password):
def login(request):
    # context = {'username': username, 'password': password}
    # return render(request, 'index.html', context)
    return render_to_response("500.html")

