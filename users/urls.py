from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("reg", views.reg, name="reg"),
    path("addCourse", views.addCourse, name="addCourse"),
    path("rmCourse", views.rmCourse, name="rmCourse"),
]
