from reg.models import Course
from django.urls import path

from . import views

app_name = "reg"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:course_id>', views.course,  name="course"),
    path('<int:course_id>/addStudent', views.addStudent, name="addStudent"),
    #path('<int:student_id>', views.student, name="student"),

]
