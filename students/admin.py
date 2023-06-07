from django.contrib import admin
from .models import Student


@admin.register(Student)
class SupplieryAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
