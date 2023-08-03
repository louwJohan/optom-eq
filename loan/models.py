from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    student_nr = models.CharField(max_length=15)
   
    


class Loan(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    equipment = models.TextField()
    equipment_taken = models.DateTimeField(auto_now_add=True)
    equipment_returned = models.DateTimeField()
