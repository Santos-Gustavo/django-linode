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


class ServiceFormView(LoginRequiredMixin, CreateView):
    model = ServiceModel
    template_name = 'my_app/service/service_form.html'
    form_class = ServiceForm
    success_url = reverse_lazy('my_app:success-page')
####################################################################################################


####################################################################################################
# Work
####################################################################################################
class WorkView(TemplateView):
    template_name = 'my_app/work/work.html'
    context_object_name = 'jobs'


class WorkTemplateView(TemplateView):
    def __init__(self, work_type):
        self.template_name = 'my_app/work/work_template.html'
        self.work_type = work_type

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = WorkModel.objects.filter(type_job=self.work_type)
        return context


class WorkConstructionView(WorkTemplateView):
    def __init__(self):
        super().__init__(work_type=1)


class WorkCleaningView(WorkTemplateView):
    def __init__(self):
        super().__init__(work_type=2)


class WorkOtherView(WorkTemplateView):
    def __init__(self):
        super().__init__(work_type=3)


class WorkFormTemplate(LoginRequiredMixin, CreateView):
    def __init__(self, form_class):
        self.model = WorkModel
        self.template_name = 'my_app/work/work_form.html'
        self.form_class = form_class
        self.success_url = reverse_lazy('my_app:success-page')


class WorkConstructionCreateView(WorkFormTemplate):
    def __init__(self):
        super().__init__(form_class=WorkConstructionForm)


class WorkCleaningCreateView(LoginRequiredMixin, CreateView):
    def __init__(self):
        super().__init__(form_class=WorkCleaningForm)


class WorkOtherCreateView(LoginRequiredMixin, CreateView):
    def __init__(self):
        super().__init__(form_class=WorkOtherForm)
####################################################################################################
