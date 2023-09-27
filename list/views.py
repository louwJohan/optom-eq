from django.shortcuts import render, reverse, redirect
from loan.models import Loan, Health, Ref, Student
import datetime


def list(request):
    return render(request, 'list.html')

def list_display(request):
    room = request.GET.get('room')
    date = datetime.date.today()
    request.session['room'] = room
    if room == "01.29a" or room == "01.09":
        list = Health.objects.filter(room=room, date=date, all_returned=False)
    else:
        list = Ref.objects.filter(room=room, date=date, all_returned=False)
    return render(request, 'list_display.html',{'list':list,
                                                'room': room
                                                })

def not_returned(request):
    room = request.GET.get('returns')
    print(room)
    ref = Ref.objects.filter(all_returned=False)
    health = Health.objects.filter(all_returned=False)
    return render(request, 'not_returned.html', {'ref':ref, 'health':health})

def edit(request, pk):
    room = request.session.get('room')
    if room == "01.29a" or room == "01.09":
        item = Health.objects.get(pk=pk)
    else:
        item = Ref.objects.get(pk=pk)
    
    if request.method == 'POST':
        if room == "01.29a" or room == "01.09":
            student_id = request.POST.get('student')
            item.student = Student.objects.get(pk=int(student_id))
            item.room = request.POST.get('room')
            item.volk = request.POST.get('volk')
            item.ophthalmoscope = request.POST.get('ophth')
            item.ant_eye = request.POST.get('anteye')
            item.post_eye = request.POST.get('posteye')
            item.focusrod = request.POST.get('focusrod')
            item.stand = request.POST.get('stand')
            item.recording_eq = request.POST.get('recording')
            item.save()
            return redirect(reverse('loan'))
        else:
            student_id = request.POST.get('student')
            item.student = Student.objects.get(pk=int(student_id))
            print(item.student)
            item.room = request.POST.get('room')
            item.ret = request.POST.get('ret')
            item.ref_box = request.POST.get('refbox')
            item.model_eye = request.POST.get('modeleye')
            item.budgy_stick = request.POST.get('budgy')
            item.pd_ruler = request.POST.get('pdruler')
            item.occluder = request.POST.get('occluder')
            item.recording_eq = request.POST.get('recording')
            item.save()
            return redirect(reverse('loan'))

    return render(request, 'edit.html',{'item': item})