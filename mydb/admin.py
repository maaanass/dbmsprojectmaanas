
from django.contrib import admin
from .models import members
from .models import emplyoee
from .models import adminlogin

admin.site.register(members)
admin.site.register(emplyoee)
admin.site.register(adminlogin)

