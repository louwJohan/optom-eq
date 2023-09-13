from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    student_nr = models.CharField(max_length=15)
    


class Loan(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.CharField(max_length=10)
    equipment = models.TextField()
    time_taken = models.DateTimeField(auto_now_add=True)
    time_returned = models.DateTimeField()
