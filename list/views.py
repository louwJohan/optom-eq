from django.shortcuts import render
from loan.models import Loan

# Create your views here.
def list(request):
    return render(request, 'list.html')

def list_display(request):
    room = request.GET.get('room')
    list = Loan.objects.filter(room=room)
    return render(request, 'list_display.html',{'list':list})