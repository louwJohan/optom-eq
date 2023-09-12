from django.shortcuts import render

# Create your views here.
def loan(request):
    return render(request, 'loan.html')

def longloan(request):
    return render(request, 'longloan.html')