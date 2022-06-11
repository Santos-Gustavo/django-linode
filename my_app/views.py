from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import WorkModel, ServiceModel
from .forms import *


class IndexView(TemplateView):
    template_name = 'my_app/index.html'


class Error404View(TemplateView):
    template_name = 'my_app/404.html'


class SuccessView(TemplateView):
    template_name = 'my_app/success.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('my_app:success-page')
    template_name = 'my_app/signup.html'


class HouseView(TemplateView):
    template_name = 'my_app/house.html'


####################################################################################################
# Service
####################################################################################################
class ServiceView(TemplateView):
    template_name = 'my_app/service/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServiceModel.objects.all()
        return context


class ServiceFormView(LoginRequiredMixin, CreateView):
    model = ServiceModel
    template_name = 'my_app/service/service_form.html'
    form_class = ServiceForm
    success_url = reverse_lazy('my_app:success-page')


class ServiceDomesticView(TemplateView):
    template_name = 'my_app/service/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServiceModel.objects.filter(type_service=1)
        return context


class ServiceHealthyBeautyView(TemplateView):
    template_name = 'my_app/service/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServiceModel.objects.filter(type_service=2)
        return context


class ServiceTransportView(TemplateView):
    template_name = 'my_app/service/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServiceModel.objects.filter(type_service=3)
        return context
####################################################################################################


####################################################################################################
# Work
####################################################################################################
class WorkView(TemplateView):
    template_name = 'my_app/work.html'
    context_object_name = 'jobs'


class WorkConstructionView(TemplateView):
    # ToDo: select only what you need in DB
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


class WorkOtherView(TemplateView):
    template_name = 'my_app/work/outros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = WorkModel.objects.filter(type_job=3)
        return context


class WorkConstructionCreateView(LoginRequiredMixin, CreateView):
    model = WorkModel
    template_name = 'my_app/work_form.html'
    form_class = WorkConstructionForm
    success_url = reverse_lazy('my_app:success-page')


class WorkCleaningCreateView(LoginRequiredMixin, CreateView):
    model = WorkModel
    template_name = 'my_app/work_form.html'
    form_class = WorkCleaningForm
    success_url = reverse_lazy('my_app:success-page')


class WorkOtherCreateView(LoginRequiredMixin, CreateView):
    model = WorkModel
    template_name = 'my_app/work_form.html'
    form_class = WorkOtherForm
    success_url = reverse_lazy('my_app:success-page')
####################################################################################################
