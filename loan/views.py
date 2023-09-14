from django.shortcuts import render
from loan.models import Student

# Create your views here.
def loan(request):
    return render(request, 'loan.html')

def longloan(request):
    students = Student.objects.all()
    return render(request, 'longloan.html', {'students': students})

def refraction(request):
    if request.method == 'POST':
        student = request.POST.get('student')
        room = request.POST.get('room')
        ret = request.POST.get('ret')
        refbox = request.POST.get('refbox')
        modeleye = request.POST.get('modeleye')
        budgy = request.POST.get('budgy')
        pdruler = request.POST.get('pdruler')
        occluder = request.POST.get('occluder')
        print(student, room, ret, refbox, modeleye, budgy, pdruler, occluder)
    students = Student.objects.all()
    return render(request, 'refraction.html', {'students': students})

def health(request):
    if request.method == 'POST':
        student = request.POST.get('student')
        room = request.POST.get('room')
        print(student, room)
    students = Student.objects.all()
    return render(request, 'health.html', {'students': students})