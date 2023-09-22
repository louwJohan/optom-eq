from django.urls import path
from list import views

urlpatterns = [
    path('', views.list, name='list'),
    path('list_display', views.list_display, name='list_display'),
    path('not_returned', views.not_returned, name='not_returned'),
]