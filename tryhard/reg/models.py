from django.db import models

# Create your models here.



class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    student_id = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.student_id}"

class Course(models.Model):
    course_id = models.IntegerField(null=True)
    course_name = models.CharField(max_length=64)
    student_list = models.ManyToManyField(Student, blank=True, related_name="subjects")

    
  

    def __str__(self):
        return f"{self.course_id} {self.course_name} "

