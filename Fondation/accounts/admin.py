from django.contrib import admin
from .models import *


# Register your models here.


class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'birthday','phone','photo','genre')


admin.site.register(Profile, AdminProfile)
