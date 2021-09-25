from django.contrib import admin

# Register your models here.
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'seat', 'maxSeat', 'credit')
    ordering = ['course_name']
    
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ("subjects",)
    list_display = ('student_id', 'credit', 'maxCredit')
    ordering = ['student_id']
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
