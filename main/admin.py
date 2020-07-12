from django.contrib import admin
from .models import Survey

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    model = Survey
    list_display = ('name', 'email', 'phone_number', 'address')
