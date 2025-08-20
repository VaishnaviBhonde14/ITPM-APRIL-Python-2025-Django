from django.db import models
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank = True,null=True)


    def __str__(self):
        return self.title
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    joined_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE,related_name = 'enrollments')
    course = models.ForeignKey(Course, on_delete = models.CASCADE,related_name = 'enrollments')
    enrollment_date = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('student' , 'course')

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"