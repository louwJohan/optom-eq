from django.shortcuts import render
from loan.models import Student

# Create your views here.
def loan(request):
    students = Student.objects.all()
    return render(request, 'loan.html', {'students': students})

def longloan(request):
    return render(request, 'longloan.html')