from django.contrib import admin
from .models import Course


@admin.register(Course)
class SupplieryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "duration")
