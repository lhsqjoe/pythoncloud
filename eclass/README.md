#First 
python version: 3.6.7 (cmd: python3 -V)
Django version: 2.1.3 (django-admin --version)

python modules:
PyMySQL 0.9.2

#create apps
python3 manage.py startapp sysuser # 系统用户模块
python3 manage.py startapp vmmanager # vm 生命周期管理


python3 manage.py migrate

python manage.py createsuperuser  # 创建后台管理超级用户  本项目  test:1

#models 有改变，如何同步
python3 manage.py makemigrations
python3 manage.py migrate


