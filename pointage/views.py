from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from .models import Employe, Pointage
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q

#gestion des permision
def require_role(role):
    def decorator(view_func):
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('authentication:login')
            if getattr(request.user, 'role', None) != role:
                messages.error(request, "Accès refusé")
                return redirect('authentication:login')
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator


@login_required
@require_role('VIGILE')
def vigile_view(request):
    employes = Employe.objects.all()
    if request.method == 'POST':
        emp_id = request.POST.get('employe_id')
        action = request.POST.get('action')  # 'IN' or 'OUT'
        try:
            emp = Employe.objects.get(pk=emp_id)
            Pointage.objects.create(employe=emp, action=action, recorded_by=request.user)
            messages.success(request, f"Pointage {action} enregistré pour {emp}")
        except Employe.DoesNotExist:
            messages.error(request, "Employé non trouvé")
        return redirect('pointage:vgl_dashboard')

    return render(request, 'pointage/vigile.html', {'employes': employes})



@login_required
@require_role('DRH')
def drh_dashboard(request):
    employes = Employe.objects.all()
    selected_id = request.GET.get('employe')
    selected = None
    pointages = None
    # Par défaut : afficher aujourd'hui
    date_from = request.GET.get('from')
    date_to = request.GET.get('to')
    if selected_id:
        selected = get_object_or_404(Employe, pk=selected_id)
        qs = selected.pointages.all()
        if date_from:
            qs = qs.filter(timestamp_date_gte=date_from)
        if date_to:
            qs = qs.filter(timestamp_date_lte=date_to)
        pointages = qs.order_by('-timestamp')
    return render(request, 'pointage/drh_detail.html', {
        'employes': employes,
        'selected': selected,
        'pointages': pointages,
    })
