from django.db import models

# Create your models here.
class Loan(models.Model):
    student = models.CharField(max_length=150)
    student_nr = models.CharField(max_length=15)
    time = models.DateField(auto_now_add=True)
    room = models.CharField(max_length=10)
    