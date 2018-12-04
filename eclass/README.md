#First 
python version: 3.6.7 (cmd: python -V)
Django version: 2.1.3 (django-admin --version)

python modules:
PyMySQL 0.9.2

#django cmd
python -m django --version # 查看版本

django-admin startproject eclass # 创建project
#create apps
python manage.py startapp sysuser # 系统用户模块
python manage.py startapp vmmanager # vm 生命周期管理


python manage.py migrate

python manage.py createsuperuser  # 创建后台管理超级用户  本项目  test:1

#models 有改变，如何同步
python manage.py sqlmigrate sysuser 0001 #控制台 显示 sql
python manage.py makemigrations
python manage.py migrate

python manage.py runserver 18000# 运行
python manage.py runserver 0:18000# 运行

python manage.py shell # 管理shell



