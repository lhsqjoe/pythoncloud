from django.urls import path
from . import views

urlpatterns = {
    path('', views.show_login, name='show_login'),
    path('login/', views.login, name='login'),

    
    # path('login/<username>/<password>/', views.login, name='login'),
    # url 例子 http://127.0.0.1:8000/sysuser/login/zhangsan/123/

}
