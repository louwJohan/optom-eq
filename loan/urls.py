from django.urls import path
from loan import views

urlpatterns = [
    path('', views.loan, name='loan'),
]