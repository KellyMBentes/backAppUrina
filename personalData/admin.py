from django.contrib import admin
from .models import PersonalData
# Register your models here.
class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'birthDate']
    list_filter = ['birthDate']
admin.site.register(PersonalData, PersonalDataAdmin)