from django.db import models

# Create your models here.
class Skill:  
  def __init__(self,level,description):
    self.level = level
    self.description = description

skills = [
  Skill(1,'Fundamental Awareness'),
  Skill(2, 'Novice'),
  Skill(3, 'Intermediate'),
]