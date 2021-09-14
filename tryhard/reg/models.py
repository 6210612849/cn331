from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Course(models.Model):
    course_id = models.IntegerField(null=True)
    course_name = models.CharField(max_length=64)
    #student_list = models.ManyToManyField(User, blank=True, related_name="subjects")

    def __str__(self):
        return f"{self.course_id} {self.course_name} "

class Student(models.Model):
    #first_name = models.CharField(max_length=64)
    #last_name = models.CharField(max_length=64)
    student_id = models.OneToOneField(User, blank=True, on_delete=models.CASCADE,)
    subjects = models.ManyToManyField(Course, blank=True, related_name="studentIn")
    credit = models.IntegerField(null=True)

    def __str__(self):
        return f" {self.student_id}"