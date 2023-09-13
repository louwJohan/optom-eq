from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    student_nr = models.CharField(max_length=15)
    
    def __str__(self):
        return self.student_nr


class Loan(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    equipment = models.TextField()
    time_taken = models.DateTimeField(auto_now_add=True)
    time_returned = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=10, default="0.00")
