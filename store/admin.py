from django.contrib import admin
from .models import GeneralInfo



@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'delivery_address', 'selected_plan', 'dietary_preference', 'Optional_Add_ons', 'token_number']






