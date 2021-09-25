
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "first/test.html")


def contact(request):
    return render(request, "first/contact.html")
