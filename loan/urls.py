from django.urls import path
from loan import views

urlpatterns = [
    path('', views.loan, name='loan'),
    path('longloan', views.longloan, name='longloan'),
    path('refraction', views.refraction, name='refraction'),
    path('health', views.health, name='health'),
    path('returns', views.returns, name='returns')
]