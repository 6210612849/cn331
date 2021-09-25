from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
# Create your models here.





class Course(models.Model):
    course_id = models.IntegerField(null=True)
    course_name = models.CharField(max_length=64)
    seat = models.IntegerField(null=True)
    maxSeat = models.IntegerField(null=True)
    credit = models.IntegerField(null=True)

    def __str__(self):
        return f"id: {self.course_id} name:{self.course_name} seatleft:{self.seat}/{self.maxSeat} credit.{self.credit}"

class Student(models.Model):
    student_id = models.OneToOneField(User, blank=True, on_delete=models.CASCADE,)
    subjects = models.ManyToManyField(Course, blank=True, related_name="subjects")
    credit = models.IntegerField(null=True)
    maxCredit = models.IntegerField(null=True)
    
    def __str__(self):
        return f" {self.student_id}"