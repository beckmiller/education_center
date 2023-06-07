from django.contrib import admin
from .models import Grade


@admin.register(Grade)
class SupplieryAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "value", "date")
