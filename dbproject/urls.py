"""
URL configuration for dbproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import os
import sys
from django.contrib import admin
from django.urls import path
from mydb.views import login,success_page,admin_success_page,adminredirect,adminloginpage,member_reset_password_page,reset_password

import sys
print(sys.path)

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(BASE_DIR)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('success/<int:user_id>/', success_page, name='success_page'),
    path('', login, name='home'),
    path('adminredirect/',adminredirect, name='adminredirect'),
    path('adminlogin/',adminloginpage, name='adminlogin'),
    path('admin_success_page/<int:user_id>/',admin_success_page,name='admin_success_page'),
    path('member_reset_password_page/<int:user_id>/', member_reset_password_page, name='member_reset_password_page'),
    path('reset_password/<int:user_id>/', reset_password, name='reset_password')
]

