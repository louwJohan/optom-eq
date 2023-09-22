from django.shortcuts import render, redirect, get_object_or_404, reverse
from loan.models import Student, Loan
from datetime import datetime

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
        equipment = f"Volk: {volk},Ophthalmoscope: {ophth},Anterior Eye: {anteye},Posterior Eye: {posteye},Focus Rod: {focusrod},Stand: {stand}"
        form = Loan(student=student,
                    room = room,
                    equipment = equipment
                    )
        form.save()
        return redirect(reverse('loan'))
        
    
    return render(request, 'health.html', {'students': students})

def returns(request,pk):
    returns = get_object_or_404(Loan, id=pk)
    equipment = returns.equipment.split(",")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    if request.method == 'POST':
        returns.equipment_returned = returns.equipment
        returns.all_returned = True
        returns.time_returned = current_time
        returns.save()
        return redirect(reverse('loan'))
    return render(request, 'returns.html',{'returns':returns, 'equipment': equipment})