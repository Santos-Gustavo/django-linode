from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.index_view, name='index-page'),
    path('work/', views.work_view, name='work-page'),
    path('work/form/', views.work_form_view, name='work-form-page'),
    path('success/', views.success_view, name='success-page'),
]
