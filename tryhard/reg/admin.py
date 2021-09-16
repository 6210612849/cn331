from django.contrib import admin

# Register your models here.
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'seat', 'credit')
#    ordering = ['coruse_id']
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ("subjects",)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
