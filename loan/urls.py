from django.urls import path
from loan import views

urlpatterns = [
    path('', views.loan, name='loan'),
    path('longloan', views.longloan, name='longloan'),
    path('refraction', views.refraction, name='refraction'),
    path('health', views.health, name='health'),
    path('returns/<int:pk>', views.returns, name='returns'),
    path('longlist', views.longList, name='longlist'),
    path('longform', views.longForm, name='longform'),
    path('longreturn/<int:pk>', views.long_returns, name='longreturn'),
]