
from django.contrib import admin
from mydb.models import members
from mydb.models import employee
from mydb.models import adminlogin

admin.site.register(members)
admin.site.register(employee)
admin.site.register(adminlogin)

