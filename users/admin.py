from django.contrib import admin
from .models import CustomUser,UserOtp
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone','is_superuser','is_active','is_user','is_staff')


admin.site.register(UserOtp)