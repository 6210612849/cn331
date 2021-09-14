from django.contrib import admin

# Register your models here.
from .models import *

#class CourseInStudent(admin.ModelAdmin):
#    list_display = ("first_name", "last_name", "student_id")
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ("subjects",)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course)
