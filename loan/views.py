from django.shortcuts import render, redirect, get_object_or_404, reverse
from loan.models import Student, Ref, Health, Long
from datetime import datetime

# Create your views here.
def loan(request):
    return render(request, 'loan.html')

def longloan(request):
    return render(request, 'longloan.html')

def longForm(request):
    students = Student.objects.all()
    if request.method == 'POST':
        student_id = request.POST.get('student')
        student = Student.objects.get(id=int(student_id))
        kit = request.POST.get('kit')
        return_date = request.POST.get('return_date')
        form = Long(student=student,
                    kit=kit,
                    return_date=return_date
                    )
        form.save()
        return redirect('longloan')
    return render(request, 'longform.html', {'students': students})

def longList(request):
    list = Long.objects.filter(returned=False)
    return render(request, 'longlist.html', {'list': list})

def long_returns(request, pk):
    item = Long.objects.get(pk=pk)
    if request.method == 'POST':
        item.returned = True
        item.save()
        return redirect(reverse('longlist'))
    return render(request, 'longreturn.html', {'item': item})

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
        recording = request.POST.get('recording')
        form = Ref(student=student,
                    room = room,
                    ret=ret,
                    ref_box=refbox,
                    model_eye=modeleye,
                    budgy_stick=budgy,
                    pd_ruler=pdruler,
                    occluder=occluder,
                    recording_eq=recording
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
        recording = request.POST.get('recording')
        form = Health(student=student,
                    room = room,
                    volk=volk,
                    ophthalmoscope=ophth,
                    ant_eye=anteye,
                    post_eye=posteye,
                    focusrod=focusrod,
                    stand=stand,
                    recording_eq=recording
                    )
        form.save()
        return redirect(reverse('loan'))
        
    
    return render(request, 'health.html', {'students': students})

def returns(request,pk):
    returns = None
    room = request.session.get('room')
    print(room)
    if room == "01.29a" or room == "01.09":
        returns = get_object_or_404(Health, pk=pk)
    else:
        returns = get_object_or_404(Ref, pk=pk)
    now = datetime.now()
    print(returns)
    current_time = now.strftime("%H:%M:%S")
    if request.method == 'POST':
        returns.all_returned = True
        returns.time_returned = current_time
        returns.save()
        return redirect(reverse('list'))
    return render(request, 'returns.html',{'returns':returns, 'room':room})