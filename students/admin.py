from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'roll_number',
        'name',
        'email',
        'course',
        'marks',
    )
    search_fields = ('name', 'roll_number', 'email')
    list_filter = ('course',)
    ordering = ('-marks',)
