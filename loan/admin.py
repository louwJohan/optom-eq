from django.contrib import admin
from loan.models import Student, Loan

# Register your models here.
admin.site.register(Loan)
admin.site.register(Student)