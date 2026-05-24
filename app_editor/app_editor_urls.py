from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('process', views.process, name = 'process')
    # path('get_duration', views.get_duration, name='get_duration'),
    
]