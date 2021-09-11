from django.shortcuts import render

# Create your views here.

from .models import Course


def index(request):
    return render(request, "reg/index.html", {
        "reg": Course.objects.all()
    })
