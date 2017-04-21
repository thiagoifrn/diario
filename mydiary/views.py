from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from .models import Diario
from .forms import DiarioForm
from .forms import FormEdit
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):
    diary = Diario.objects.filter(usuario=request.user).order_by('data_entrada')
    return render(request, 'mydiary/post_list.html', {"diario":diary})
@login_required
def post_new(request):
    form = DiarioForm(request.POST)
    if form.is_valid():
        diario = form.save(commit=False)
        diario.usuario = request.user
        diario.save()
        return render(request, 'mydiary/sucess.html')
    else:
        form = DiarioForm()
    return render(request, 'mydiary/post_edit.html', {'form': form})
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Diario, pk=pk)
    return render(request, 'mydiary/post_detail.html', {'diario': post})
@login_required
def post_edit(request, pk):
    diario = get_object_or_404(Diario, pk=pk)
    if request.method == "POST":
        form = FormEdit(request.POST, instance=diario)
        if form.is_valid():
            diario = form.save(commit=False)
            date_today = datetime.today()
            diario.data_saida=date_today
            diario.save()
            return redirect('post_detail', pk=diario.pk)
    else:
        form = FormEdit(instance=diario)
    return render(request, 'mydiary/post_edit.html', {'form': form})
@login_required
def dashboard(request):
    date_today = datetime.today()
    diario = Diario.objects.filter(usuario=request.user, data_entrada__year=date_today.year, data_entrada__month=date_today.month, data_entrada__day=date_today.day).last()

    return render(request, 'mydiary/dashboard.html', {'diario': diario})

