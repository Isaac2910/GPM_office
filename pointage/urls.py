from django.urls import path
from . import views

app_name = 'pointage'

urlpatterns = [
    path('vigile/', views.vigile_view, name='vgl_dashboard'),
    path('drh/', views.drh_dashboard, name='drh_dashboard'),
]