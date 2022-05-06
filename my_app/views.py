from django.urls import reverse_lazy
from django.shortcuts import render, reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, FormView, CreateView, ListView
from .forms import *
from .models import WorkModel


class IndexView(TemplateView):
    template_name = 'my_app/index.html'


class SuccessView(TemplateView):
    template_name = 'my_app/success.html'


class WorkView(TemplateView):
    template_name = 'my_app/work.html'
    context_object_name = 'jobs'


class Construction(TemplateView):
    template_name = 'my_app/work/construction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = WorkModel.objects.filter(type_job=1)
        return context


class WorkCreateView(CreateView):
    model = WorkModel
    template_name = 'my_app/work_form.html'
    form_class = WorkConstructionForm
    success_url = reverse_lazy('my_app:success-page')
