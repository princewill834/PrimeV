from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date','sharer','shared')

@admin.register(CouponCode)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'code', 'valid','active')

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone', 'email')
