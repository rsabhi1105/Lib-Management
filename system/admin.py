from django.contrib import admin

from system.models import ManagementStaff


# Register your models here.

@admin.register(ManagementStaff)
class ManagementStaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')
