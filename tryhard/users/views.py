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
    #messages.success(request, "Logged in desu")
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
    
    stu = Student.objects.get(pk=(request.user.id)).subjects.all()
    notCourse = Course.objects.exclude(pk__in=stu)
    
    return render(request, "users/reg.html", {
        "notCourse": notCourse,
        "stu": stu,

    })

def addCourse(request):
    if request.method == "POST":
        stu = Student.objects.get(pk=(request.user.id))
        course = request.POST["course"]
        stu = stu.subjects.add(course)
    return HttpResponseRedirect(reverse("users:reg"))

def rmCourse(request):
    if request.method == "POST":
        stu = Student.objects.get(pk=(request.user.id))
        course = request.POST["course"]
        stu = stu.subjects.remove(course)
    return HttpResponseRedirect(reverse("users:reg"))