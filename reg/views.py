
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.

from .models import Course, Student


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    else:
        return render(request, "reg/index.html", {
            "reg": Course.objects.all()
        })


def course(request, course_id):
    c = get_object_or_404(Course, pk=course_id)
    return render(request, "reg/course.html", {
        "course": c,
        "student": c.studentIn.all(),
        "student_not": Student.objects.exclude(subjects=c).all()
    })


def addStudent(request, course_id):
    if request.method == "POST":
        course = get_object_or_404(Course, pk=course_id)
        student = request.POST["student"]
        course = course.student_list.add(student)
    return HttpResponseRedirect(reverse("reg:course", args=(course_id,)))
    # return render(request, "reg/course.html"),{
    #        "testvar": "this is text"
    # }


def addCourse(request, student_id):
    if request.method == "POST":
        student = get_object_or_404(Student, pk=student_id)
        student = request.POST["student"]
        course = course.student_list.add(student)

    return HttpResponseRedirect(reverse("reg:course", args=(course_id,)))
# def student(request, student_id):
#    return None
