from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomAdmin(UserAdmin):
    list_display =('email','fullname','username','coupon','referer','total_balance','task_earned','tot_referer','is_staff','is_admin')
    search_fields =('email','fullname','username')
    readonly_fields =('date_joined','last_login')

    filter_horizontal = ()
    list_filter =()
    fieldsets=()

admin.site.register(Account, CustomAdmin)
