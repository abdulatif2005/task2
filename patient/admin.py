from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Patient, Diagnose


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ["is_doctor"]}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ["is_doctor"]}),)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Patient)
admin.site.register(Diagnose)
