# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    EMPLOYE = 'EMPLOYE'
    VIGILE = 'VIGILE'
    DRH = 'DRH'

    ROLE_CHOICES = (
        (EMPLOYE, 'employé'),
        (VIGILE, 'vigile'),
        (DRH, 'ressources humaines'),
    )
    
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')