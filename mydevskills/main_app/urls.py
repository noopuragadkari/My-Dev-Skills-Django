from django.urls import path
from .import views

urlpatterns = [
    #http://localhost:8000
    path('', views.home, name='home'),
    path('skills/', views.skills_index, name='index'),
    
]