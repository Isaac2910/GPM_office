from django.contrib import admin
from .models import Employe, Pointage

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('matricule','name', 'poste')

@admin.register(Pointage)
class PointageAdmin(admin.ModelAdmin):
    list_display = ('employe', 'action', 'timestamp', 'recorded_by')
    list_filter = ('action','timestamp')