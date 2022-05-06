from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import *
from .models import WorkModel


class IndexView(TemplateView):
    template_name = 'my_app/index.html'


class SuccessView(TemplateView):
    template_name = 'my_app/success.html'


class WorkView(TemplateView):
    template_name = 'my_app/work.html'
    context_object_name = 'jobs'


class WorkConstructionView(TemplateView):
    template_name = 'my_app/work/construction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = WorkModel.objects.filter(type_job=1)
        return context


class WorkCleaningView(TemplateView):
    template_name = 'my_app/work/cleaning.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = WorkModel.objects.filter(type_job=2)
        return context


class WorkConstructionCreateView(CreateView):
    model = WorkModel
    template_name = 'my_app/work_form.html'
    form_class = WorkConstructionForm
    success_url = reverse_lazy('my_app:success-page')


class WorkCleaningCreateView(CreateView):
    model = WorkModel
    template_name = 'my_app/work_form.html'
    form_class = WorkCleaningForm
    success_url = reverse_lazy('my_app:success-page')
