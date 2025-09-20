from django.db import models
from django.conf import settings

class Employe(models.Model):
    matricule = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    

    def _str_(self):
        return f"{self.name} {self.matricule}"

class Pointage(models.Model):
    ACTION_CHOICES = (
        ('IN', 'Entrée'),
        ('OUT', 'Sortie'),
    )
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='pointages')
    action = models.CharField(max_length=3, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    recorded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def _str_(self):
        return f"{self.employe} {self.get_action_display()} @ {self.timestamp}"