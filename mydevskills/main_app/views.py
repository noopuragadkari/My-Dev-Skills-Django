from django.shortcuts import render
from django.http import HttpResponse

from django.db import models
# Create your models here.
class Skill:  
  def __init__(self,level,description):
    self.level = level
    self.description = description

skills = [
  Skill(1,'Fundamental Awareness'),
  Skill(2, 'Novice'),
  Skill(3, 'Intermediate')
]

def home(request):
    return render(request, 'home.html')

def skills_index(request):
  return render(request, 'skills/index.html',{'skills':skills})