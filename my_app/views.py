from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import WorkModel, ServiceModel
from .forms import *


class IndexView(TemplateView):
    template_name = 'my_app/index.html'


def handle_not_found(request, exception=None):
    return render(request, 'my_app/404.html')


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
class ServiceTemplateView(TemplateView):
    def __init__(self, service_type):
        self.template_name = 'my_app/service/service.html'
        self.service_type = service_type

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.service_type == 0:
            context['services'] = ServiceModel.objects.all()
        else:
            context['services'] = ServiceModel.objects.filter(type_service=self.service_type)
        return context


class ServiceView(ServiceTemplateView):
    def __init__(self):
        super().__init__(service_type=0)
    
    
class ServiceDomesticView(ServiceTemplateView):
    def __init__(self):
        super().__init__(service_type=1)


class ServiceHealthyBeautyView(ServiceTemplateView):
    def __init__(self):
        super().__init__(service_type=2)


class ServiceTransportView(ServiceTemplateView):
    def __init__(self):
        super().__init__(service_type=3)


class ServiceFoodView(ServiceTemplateView):
    def __init__(self):
        super().__init__(service_type=4)


class ServiceClassView(ServiceTemplateView):
    def __init__(self):
        super().__init__(service_type=5)


class ServiceTravelView(ServiceTemplateView):
    def __init__(self):
        super().__init__(service_type=6)


class ServiceTechnicView(ServiceTemplateView):
    def __init__(self):
        super().__init__(service_type=7)


class ServiceOtherView(ServiceTemplateView):
    def __init__(self):
        super().__init__(service_type=20)


class ServiceFormView(LoginRequiredMixin, CreateView):
    model = ServiceModel
    template_name = 'my_app/service/service_form.html'
    form_class = ServiceForm
    success_url = reverse_lazy('my_app:success-page')
####################################################################################################


####################################################################################################
# Work
####################################################################################################
class WorkTemplateView(TemplateView):
    def __init__(self, work_type, template_name):
        self.template_name = template_name
        self.work_type = work_type

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.work_type == 0:
            context['jobs'] = WorkModel.objects.all()
        else:
            context['jobs'] = WorkModel.objects.filter(type_job=self.work_type)
        return context


class WorkView(WorkTemplateView):
    def __init__(self):
        super().__init__(work_type=0, template_name='my_app/work/work.html')


class WorkConstructionView(WorkTemplateView):
    def __init__(self):
        super().__init__(work_type=1, template_name='my_app/work/work_construction.html')


class WorkCleaningView(WorkTemplateView):
    def __init__(self):
        super().__init__(work_type=2, template_name='my_app/work/work_cleaning.html')


class WorkOtherView(WorkTemplateView):
    def __init__(self):
        super().__init__(work_type=3, template_name='my_app/work/work_others.html')


class WorkFormTemplate(LoginRequiredMixin, CreateView):
    def __init__(self, form_class):
        # For some reason specify template_name here doesn't work, must investigate
        self.model = WorkModel
        self.form_class = form_class
        self.success_url = reverse_lazy('my_app:success-page')


class WorkConstructionCreateView(WorkFormTemplate):
    def __init__(self):
        super().__init__(form_class=WorkConstructionForm)
        self.template_name = 'my_app/work/work_form.html'


class WorkCleaningCreateView(LoginRequiredMixin, CreateView):
    def __init__(self):
        super().__init__(form_class=WorkCleaningForm)
        self.template_name = 'my_app/work/work_form.html'


class WorkOtherCreateView(LoginRequiredMixin, CreateView):
    def __init__(self):
        super().__init__(form_class=WorkOtherForm)
        self.template_name = 'my_app/work/work_form.html'
####################################################################################################
