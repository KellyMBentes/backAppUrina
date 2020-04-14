from django.contrib import admin
from .models import QuestionForm, Option

admin.site.register(Option)
admin.site.register(QuestionForm)
