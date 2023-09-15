from django.urls import path
from list import views

urlpatterns = [
    path('', views.list, name='list'),
    path('list_display', views.ListDisplay.as_view(), name='list_display')
]