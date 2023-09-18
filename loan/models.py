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
    equipment = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    time_taken = models.TimeField(auto_now_add=True)
    time_returned = models.TimeField(auto_now_add=False, default='12:00')
    room = models.CharField(max_length=10, default="0.00")
    equipment_returned = models.CharField(max_length=250, default="None")
    all_returned = models.BooleanField(default=False)

    def __str__(self):
        return self.student.student_nr