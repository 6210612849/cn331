from django.contrib import admin

# Register your models here.
from .models import *

class CourseInStudent(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "student_id")
class StudentInCourse(admin.ModelAdmin):
    filter_horizontal = ("student_list",)
admin.site.register(Student, CourseInStudent)
admin.site.register(Course, StudentInCourse)
