
from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Course, Student


def index(request):
    return render(request, "reg/index.html", {
        "reg": Course.objects.all()
    })

def course(request, course_id):
    c = get_object_or_404(Course, pk=course_id)
    return render(request, "reg/course.html", {
        "course": c,
        #"notInCourse": Student.objects.exclude(subjects=course_id).all(),
    })

def addStudent(request, course_id):
    return None
#def student(request, student_id):
#    return None