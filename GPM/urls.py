
from django.contrib import admin
from django.urls import path , include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda r: redirect('authentication:login')),
    path('auth/', include('authentication.urls', namespace='auth')),
    #path('ptg', include('pointage.urls'))
]
