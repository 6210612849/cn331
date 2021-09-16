from reg.models import Course, Student
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    else:
        return render(request, "users/index.html")


def login_view(request):
    # messages.success(request, "Logged in desu")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            messages.warning(request, "Invalid credential.")
            return render(request, "users/login.html", {
                "messages": messages.get_messages(request)
            })
    return render(request, "users/login.html")

    """
    if "next" in request.GET:
        next = request.GET["next"]
    else:
        next = reverse("users:index")

    return render(request, "users/login.html", {
        "next": next
    })
    """


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return render(request, "users/login.html", {
        "messages": messages.get_messages(request)
    })


def reg(request):

    stu = Student.objects.get(pk=request.user.id).subjects.all()
    print(stu)
    studentUser = Student.objects.get(pk=(request.user.id))
    notCourse = Course.objects.exclude(pk__in=stu)
    return render(request, "users/reg.html", {
        "stu": stu,
        "studentUser": studentUser,
        "notCourse": notCourse,

    })


def addCourse(request):
    if request.method == "POST":
        student = Student.objects.get(pk=(request.user.id))
        course = request.POST["course"]

        student_credit = Student.objects.get(pk=(request.user.id)).credit
        student_seat = 1
        course_credit = Course.objects.get(pk=(course)).credit
        course_seat = Course.objects.get(pk=(course)).seat

        if (student_credit >= course_credit) and (course_seat > 0):
            student_credit = student_credit - course_credit
            course_seat = course_seat - student_seat
            Student.objects.filter(pk=request.user.id).update(
                credit=student_credit)
            Course.objects.filter(pk=(course)).update(seat=course_seat)
            student = student.subjects.add(course)
            return HttpResponseRedirect(reverse("users:reg"))
        else:
            return HttpResponseRedirect(reverse("users:reg"))


def rmCourse(request):
    if request.method == "POST":
        stu = Student.objects.get(pk=(request.user.id))
        course = request.POST["course"]

        course_credit = Course.objects.get(pk=(course)).credit
        student_credit = Student.objects.get(pk=(request.user.id)).credit
        student_seat = 1
        course_seat = Course.objects.get(pk=(course)).seat

        student_credit = student_credit + course_credit
        course_seat = course_seat + student_seat
        Student.objects.filter(pk=request.user.id).update(
            credit=student_credit)
        Course.objects.filter(pk=(course)).update(seat=course_seat)
        stu = stu.subjects.remove(course)
        return HttpResponseRedirect(reverse("users:reg"))


def change(request):

    return render(request, "users/change.html")
