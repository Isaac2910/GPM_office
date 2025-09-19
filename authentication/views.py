from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm 


#funnction de connexion selon les roles
def login_view(request):
    if request.user.is_authenticated:
        # rediriger selon rôle si déjà connecté
        if hasattr(request.user, 'role') and request.user.role == 'VIGILE':
            return redirect('pointage:vgl_dashboard')
        elif hasattr(request.user, 'role') and request.user.role == 'DRH':
            return redirect('pointage:drh_dashboard')
        else:
            return redirect('pointage:vgl_dashboard')

    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            if getattr(user, 'role', None) == 'VIGILE':
                return redirect('pointage:vgl_dashboard')
            elif getattr(user, 'role', None) == 'DRH':
                return redirect('pointage:drh_dashboard')
            else:
                return redirect('pointage:vigile')
        else:
            messages.error(request, 'Identifiants invalides')
    return render(request, 'auth/login.html', {'form': form})

#function de deconnexion 
def logout_view(request):
    logout(request)
    return redirect('authentication:login')
            



    



