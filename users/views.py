from reg.models import Course, Student
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
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

    #stu = Student.objects.get(pk=request.user.id).subjects.all()
    stu = get_object_or_404(Student, student_id=request.user).subjects.all()

    studentUser = Student.objects.get(student_id=request.user)
    notCourse = Course.objects.exclude(pk__in=stu)

    stu_list = []
    for c in stu:
        stu_list.append(c)
    return render(request, "users/reg.html", {
        "stu": stu_list,
        "studentUser": studentUser,
        "notCourse": notCourse,

    })


def addCourse(request):
    if request.method == "POST":
        student = Student.objects.get(student_id=request.user)
        course = request.POST["course"]
        if course != "":
            student_credit = Student.objects.get(student_id=request.user).credit
            student_seat = 1
            course_credit = Course.objects.get(pk=(course)).credit
            course_seat = Course.objects.get(pk=(course)).seat

            if (student_credit >= course_credit) and (course_seat > 0):
                student_credit = student_credit - course_credit
                course_seat = course_seat - student_seat
                Student.objects.filter(student_id=request.user).update(
                    credit=student_credit)
                Course.objects.filter(pk=(course)).update(seat=course_seat)
                student = student.subjects.add(course)
    return HttpResponseRedirect(reverse("users:reg"))


def rmCourse(request):
    print(request.POST)
    if request.method == "POST":
        student = Student.objects.get(student_id=request.user)
        c = request.POST["course"]
        if c != "":
            course_credit = Course.objects.get(pk=(c)).credit
            student_credit = Student.objects.get(student_id=request.user).credit
            student_seat = 1
            course_seat = Course.objects.get(pk=(c)).seat
            course_maxSeat = Course.objects.get(pk=(c)).maxSeat

            if (course_seat <= course_maxSeat):
                student_credit = student_credit + course_credit
                course_seat = course_seat + student_seat
                Student.objects.filter(student_id=request.user).update(
                    credit=student_credit)
                Course.objects.filter(pk=(c)).update(seat=course_seat)
                student = student.subjects.remove(c)

    return HttpResponseRedirect(reverse("users:reg"))
