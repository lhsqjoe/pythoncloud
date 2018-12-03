from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


def show_login(request):
    # print(SysUser.objects.all())
    # return HttpResponse("Hello,world. You are at the polls index1")
    return render(request, "login.html")


# 用户登录
# def login(request,username, password):

def login(request):
    context = {'username': 'zhangSan', 'password': 'lisi'}
    # context = {'username': username, 'password': password}
    # return render(request, 'index.html', context)
    # raise Http404("Question does not exist")
    # return render(request, "index.html", Context({'username':'zhangsan'}))
    return render(request, "index.html", context)

