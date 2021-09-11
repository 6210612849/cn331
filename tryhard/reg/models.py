from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    student_id = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.student_id}"


class Course(models.Model):
    course_name = models.CharField(max_length=64)
    student_list = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="member")

    def __str__(self):
        return f"{self.course_name} have {self.student_list} "
