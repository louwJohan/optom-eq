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
    

class Ref(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time_taken = models.TimeField(auto_now_add=True)
    room = models.CharField(max_length=10, default="0.00")
    ref_box = models.CharField(max_length=10)
    ret = models.CharField(max_length=10)
    model_eye = models.CharField(max_length=10)
    budgy_stick = models.BooleanField(default=False, null=True)
    pd_ruler = models.BooleanField(default=False, null=True)
    occluder = models.BooleanField(default=False, null=True)
    recording_eq = models.CharField(max_length=10, null=True)
    time_returned = models.TimeField(auto_now_add=False, default='12:00')
    all_returned = models.BooleanField(default=False)

    def __str__(self):
        return self.student.student_nr
    
class Health(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time_taken = models.TimeField(auto_now_add=True)
    room = models.CharField(max_length=10, default="0.00")
    volk = models.CharField(max_length=10)
    ophthalmoscope = models.CharField(max_length=10)
    ant_eye = models.CharField(max_length=10)
    post_eye = models.CharField(max_length=10)
    focusrod = models.CharField(max_length=10)
    stand = models.BooleanField(default=False)
    recording_eq = models.CharField(max_length=10, null=True)
    time_returned = models.TimeField(auto_now_add=False, default='12:00')
    all_returned = models.BooleanField(default=False)

    def __str__(self):
        return self.student.student_nr