from django.contrib import admin
from .models import StudentModel

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','student_firstname','student_lastname','student_number','student_address','student_fee']