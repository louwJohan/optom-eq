from django.shortcuts import render
from django.views.generic import DetailView, ListView
from loan.models import Loan

# Create your views here.
def list(request):
    return render(request, 'list.html')

class ListDisplay(ListView):
    model = Loan
    template_name = 'list_display.html'
    context_object_name = 'room'

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = self.request.GET['room']
        print(context)
        return context