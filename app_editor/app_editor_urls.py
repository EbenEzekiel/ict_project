from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sundays', views.sundays, name='sundays'),
    path('process', views.process, name = 'process'),
    path('splice', views.splice, name='splice'),
    # path('get_duration', views.get_duration, name='get_duration'),
    
]