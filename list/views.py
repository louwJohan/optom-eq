from django.shortcuts import render
from loan.models import Loan
import datetime

# Create your views here.
def list(request):
    return render(request, 'list.html')

def list_display(request):
    room = request.GET.get('room')
    date = datetime.date.today()
    list = Loan.objects.filter(room=room, date=date)
    return render(request, 'list_display.html',{'list':list})