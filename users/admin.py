from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SeniorUser, JuniorUser

admin.site.register(CustomUser, UserAdmin)
admin.site.register(SeniorUser)
admin.site.register(JuniorUser)

