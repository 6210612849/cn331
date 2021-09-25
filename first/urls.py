from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "first"
urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
]
