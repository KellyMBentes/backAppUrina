from django.contrib import admin
from .models import CustomUser
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_filter = ['last_login', 'date_joined']
admin.site.register(CustomUser, UserAdmin)
