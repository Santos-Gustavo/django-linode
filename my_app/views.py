from django.urls import reverse_lazy
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


class WorkCreateView(CreateView):
    model = WorkModel
    fields = '__all__'
    success_url = reverse_lazy('my_app:success')


# class WorkFormView(FormView):
#     form_class = Work
#     template_name = 'my_app/workmodel_form.html'
#
#     success_url = reverse_lazy('my_app:success')
#
#     def form_valid(self, form):
#         return super().form_valid(form)
#         # if request.method == 'POST':
#         #     if form.is_valid():
#         #         form.type_job = type_job_value
#         #         form.save()
#         #         return HttpResponseRedirect(reverse('my_app:success-page'))
#         # else:
#         #     form = form_model
#         # return render(request, 'my_app/workmodel_form.html', context={'form': form})


class Construction(TemplateView):
    # all_jobs = WorkModel.objects.all()
    template_name = 'my_app/work/construction.html'
    # context = {'jobs': all_jobs}
#
#     @staticmethod
#     def cleaning(request):
#         all_jobs = models.WorkModel.objects.all()
#         return render(request, 'my_app/work/cleaning.html', context={'jobs': all_jobs})
#
