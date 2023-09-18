from django.shortcuts import render, redirect, reverse
from loan.models import Student, Loan

# Create your views here.
def loan(request):
    return render(request, 'loan.html')

def longloan(request):
    students = Student.objects.all()
    return render(request, 'longloan.html', {'students': students})

def refraction(request):
    students = Student.objects.all()
    if request.method == 'POST':
        student_id = request.POST.get('student')
        student = Student.objects.get(id=int(student_id))
        room = request.POST.get('room')
        ret = request.POST.get('ret')
        refbox = request.POST.get('refbox')
        modeleye = request.POST.get('modeleye')
        budgy = request.POST.get('budgy')
        pdruler = request.POST.get('pdruler')
        occluder = request.POST.get('occluder')
        equipment = f"Retniscope: {ret},\nModel Eye: {modeleye},\nRefraction Box: {refbox},\nBudgy Stick: {budgy},\nPD Ruler: {pdruler},\nOccluder: {occluder}"
        form = Loan(student=student,
                    room = room,
                    equipment = equipment
                    )
        form.save()
        return redirect(reverse('loan'))
    
    return render(request, 'refraction.html', {'students': students})

def health(request):
    students = Student.objects.all()
    if request.method == 'POST':
        student_id = request.POST.get('student')
        student = Student.objects.get(id=int(student_id))
        room = request.POST.get('room')
        volk = request.POST.get('volk')
        ophth = request.POST.get('ophth')
        anteye = request.POST.get('anteye')
        posteye = request.POST.get('posteye')
        focusrod = request.POST.get('focusrod')
        stand = request.POST.get('stand')
        equipment = f"Volk: {volk},\nOphthalmoscope: {ophth},\nAnterior Eye: {anteye},\nPosterior Eye: {posteye},\nFocus Rod: {focusrod},\nStand: {stand}"
        form = Loan(student=student,
                    room = room,
                    equipment = equipment
                    )
        form.save()
        return redirect(reverse('loan'))
        
    
    return render(request, 'health.html', {'students': students})