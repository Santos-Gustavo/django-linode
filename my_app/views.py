from django.shortcuts import render
from .forms import WorkForm
from . import models


def index_view(request):
    # my_app/templates/my_app/index.html
    return render(request, 'my_app/index.html')


def work_view(request):
    all_jobs = models.WorkModel.objects.all()
    return render(request, 'my_app/work.html', context={'jobs': all_jobs})


def work_form_view(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WorkForm()
    return render(request, 'my_app/work/work_form.html', context={'form': form})
